import uuid

class GameManager:
    def __init__(self):
        self.games = {}  # game_id -> game data

    def create_game(self):
        game_id = str(uuid.uuid4())[:8]
        player_id = str(uuid.uuid4())[:8]
        self.games[game_id] = {
            "board": [""] * 9,
            "players": [player_id],
            "turn": player_id,
            "winner": None,
        }
        return game_id, player_id

    def join_game(self, game_id: str):
        game = self.games.get(game_id)
        if not game:
            raise ValueError("Game not found")
        if len(game["players"]) >= 2:
            raise ValueError("Game already full")

        player_id = str(uuid.uuid4())[:8]
        game["players"].append(player_id)
        return player_id

    def make_move(self, game_id: str, player_id: str, position: int):
        game = self.games.get(game_id)
        if not game:
            raise ValueError("Game not found")

        if game["winner"]:
            raise ValueError("Game already finished")

        if player_id != game["turn"]:
            raise ValueError("Not your turn")

        if position < 0 or position >= 9 or game["board"][position] != "":
            raise ValueError("Invalid move")

        symbol = "X" if game["players"][0] == player_id else "O"
        game["board"][position] = symbol

        # check winner
        winner = self.check_winner(game["board"])
        if winner:
            game["winner"] = player_id

        # switch turn
        other = game["players"][0] if player_id != game["players"][0] else game["players"][1]
        game["turn"] = other
        return game

    def get_state(self, game_id: str):
        return self.games.get(game_id)

    @staticmethod
    def check_winner(board):
        wins = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for a,b,c in wins:
            if board[a] != "" and board[a] == board[b] == board[c]:
                return True
        return False
