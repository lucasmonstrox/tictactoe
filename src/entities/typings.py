from typing import Literal


CircleOrCross = Literal['x', 'o']
GameResult = Literal[CircleOrCross, 'draw', None]
Move = tuple[int, int]
MoveList = list[Move]
