import streamlit as st
import requests
import time
import os

# Auto-detect backend URL
BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")

# Avoid duplicate key errors by giving each button a session-unique prefix
def unique_key(prefix, index):
    return f"{prefix}_{index}_{st.session_state.get('player_id', 'anon')}"

def create_game():
    res = requests.post(f"{BASE_URL}/create_game")
    data = res.json()
    st.session_state["game_id"] = data["game_id"]
    st.session_state["player_id"] = data["player_id"]
    st.success(f"Game created! ID: {data['game_id']}")
    st.info("Share this Game ID with your friend to join.")


def join_game(game_id):
    res = requests.post(f"{BASE_URL}/join_game/{game_id}")
    if res.status_code == 200:
        data = res.json()
        st.session_state["game_id"] = data["game_id"]
        st.session_state["player_id"] = data["player_id"]
        st.success(f"Joined game {game_id}")
    else:
        st.error(res.json().get("detail", "Failed to join"))


def make_move(pos):
    payload = {
        "player_id": st.session_state["player_id"],
        "position": pos,
    }
    res = requests.post(f"{BASE_URL}/make_move/{st.session_state['game_id']}", json=payload)
    if res.status_code != 200:
        st.warning(res.json().get("detail", "Move failed"))


def get_state():
    res = requests.get(f"{BASE_URL}/get_state/{st.session_state['game_id']}")
    if res.status_code == 200:
        return res.json()
    return None


def render_board(state):
    board = state["board"]
    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            i = row * 3 + col
            symbol = board[i] if board[i] != "" else " "
            btn_key = unique_key("btn", i)
            if cols[col].button(symbol, key=btn_key):
                make_move(i)


# --- Streamlit UI ---
st.title("🎮 Multiplayer Tic-Tac-Toe")

if "game_id" not in st.session_state:
    st.session_state["game_id"] = None
if "player_id" not in st.session_state:
    st.session_state["player_id"] = None

if not st.session_state["game_id"]:
    st.subheader("Start or Join a Game")
    if st.button("Create New Game"):
        create_game()

    game_id_input = st.text_input("Enter Game ID to join an existing game")
    if st.button("Join Game"):
        if game_id_input:
            join_game(game_id_input)
        else:
            st.warning("Enter a valid Game ID")

else:
    st.subheader(f"Game ID: {st.session_state['game_id']}")
    st.caption(f"Your Player ID: {st.session_state['player_id']}")

    placeholder = st.empty()
    # Streamlit-safe refresh loop using rerun instead of infinite while
    while True:
        state = get_state()
        if not state:
            st.error("Game not found or ended.")
            break

        with placeholder.container():
            st.write(f"Turn: {state['turn']}")
            render_board(state)
            if state["winner"]:
                st.success(f"Winner: {state['winner']}")
                break

        time.sleep(2)
