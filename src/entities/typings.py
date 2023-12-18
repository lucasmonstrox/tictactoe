from typing import Literal


CircleOrCross = Literal['x', 'o']
DrawOrShape = Literal[CircleOrCross, 'draw', None]
Move = tuple[int, int]
MoveList = list[Move]
