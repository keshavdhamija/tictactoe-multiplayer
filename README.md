# Multiplayer Tic-Tac-Toe game made for LILA Backend Assignment.

<!-- i used chatgpt -->

## Features
- Copen 2 tabs, hit 'create game' on one tab. game_id will be generated, copy it, paste it in the same tab as well as in the other tab and hit 'join game' on both tabs. switch between tabs to make moves. works like a normal tic-tac-toe game.
- there is one streamlit but that won't go away. it stays at the bottom of the browser screen. doesn't affect the flow of the game.
- need to double click on a button to enter 'x' or 'o' in the game (another annoying streamlit problem)

The backend holds:
- `/create_game` — start a new game  
- `/join_game/{game_id}` — join existing game  
- `/make_move/{game_id}` — make a move  
- `/get_state/{game_id}` — get board + turn + winner 


Project Structure

tictactoe/
├── main.py # FastAPI backend entry
├── game_manager.py # Core game logic
├── models.py # Pydantic models
├── frontend.py # Streamlit UI
├── requirements.txt
└── README.md




Local Setup

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start backend
uvicorn main:app --reload

# Start frontend (new terminal)
streamlit run frontend.py
