from fastapi import FastAPI, HTTPException
from models import CreateGameResponse, JoinGameResponse, MoveRequest, GameStateResponse
from game_manager import GameManager

app = FastAPI(title="Multiplayer Tic-Tac-Toe")
manager = GameManager()


@app.post("/create_game", response_model=CreateGameResponse)
def create_game():
    game_id, player_id = manager.create_game()
    return {"game_id": game_id, "player_id": player_id}


@app.post("/join_game/{game_id}", response_model=JoinGameResponse)
def join_game(game_id: str):
    try:
        player_id = manager.join_game(game_id)
        return {"game_id": game_id, "player_id": player_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/make_move/{game_id}")
def make_move(game_id: str, move: MoveRequest):
    try:
        state = manager.make_move(game_id, move.player_id, move.position)
        return state
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/get_state/{game_id}", response_model=GameStateResponse)
def get_state(game_id: str):
    state = manager.get_state(game_id)
    if not state:
        raise HTTPException(status_code=404, detail="Game not found")
    return state
