from pydantic import BaseModel
from typing import Optional, List

class CreateGameResponse(BaseModel):
    game_id: str
    player_id: str

class JoinGameResponse(BaseModel):
    game_id: str
    player_id: str

class MoveRequest(BaseModel):
    player_id: str
    position: int

class GameStateResponse(BaseModel):
    board: List[str]
    players: List[str]
    turn: str
    winner: Optional[str]
