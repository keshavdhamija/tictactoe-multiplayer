# Multiplayer Tic-Tac-Toe game made for LILA Backend Assignment.

open the game from this url https://tictactoe-multiplayer-keshav.streamlit.app/
backend is hosted on render https://tictactoe-multiplayer-ti4j.onrender.com/
api docs https://tictactoe-multiplayer-ti4j.onrender.com/docs
source code is here https://github.com/keshavdhamija/tictactoe-multiplayer

## Features/ "Not Bugs"
- open 2 tabs of this url https://tictactoe-multiplayer-keshav.streamlit.app/ 
hit 'create game' on one tab. game_id will be generated. copy it, paste it in the same tab as well as in the other tab and hit 'join game' on both tabs. switch between tabs to make moves. works like a normal tic-tac-toe game.

- an error comes up. it looks like failure (it's not.) ignore it. it stays at the bottom of the browser screen. doesn't affect the flow of the game.
- every button needs to be double clicked. every button.(another annoying streamlit problem)

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
