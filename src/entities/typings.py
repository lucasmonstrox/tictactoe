from typing import Literal


MoveShape = Literal['x', 'o']
GameResult = Literal[MoveShape, 'draw', None]
Move = tuple[int, int]
MoveList = list[Move]
