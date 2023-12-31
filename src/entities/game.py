import numpy as np
from ..errors import Gameover, InvalidMove, MoveIsBusy
from .typings import MoveShape, GameResult, Move, MoveList


class Game:
    board: np.ndarray
    currentMoveShape: MoveShape
    moves: MoveList
    minimumMovesToHaveWinner: int
    maximumMovesUntilEnd: int
    result: GameResult

    def __init__(self, moves: MoveList | None = None):
        self.board = np.full((3, 3), '', dtype=np.str_)
        self.currentMoveShape = 'o'
        self.minimumMovesToHaveWinner = 5
        self.maximumMovesUntilEnd = 9
        self.moves = []
        self.result = None
        if moves is not None:
            for move in moves:
                self.addMove(move)

    def addMove(self, move: Move):
        if self.gameover():
            raise Gameover()
        if not self.isValidMove(move):
            raise InvalidMove(move)
        if not self.isFreeMove(move):
            raise MoveIsBusy(move)
        self.moves.append(move)
        x, y = move
        self.currentMoveShape = self.getNextMoveShape()
        self.board[y, x] = self.currentMoveShape
        if not self.hasMinimumMovesToHaveWinner():
            return
        if self.moveDidWin(self.currentMoveShape, move):
            self.result = self.currentMoveShape
            return
        if not self.reachedMaximumMoves():
            return
        self.result = 'draw'

    # TODO: add unit tests
    def gameover(self) -> bool:
        return self.result is not None

    def getNextMoveShape(self) -> MoveShape:
        return 'x' if self.currentMoveShape == 'o' else 'o'

    def hasMinimumMovesToHaveWinner(self) -> bool:
        return len(self.moves) >= self.minimumMovesToHaveWinner

    def isFreeMove(self, move: Move) -> bool:
        x, y = move
        return self.board[y, x] == ''

    def isValidMove(self, move: Move) -> bool:
        minimumXYAxis = 0
        maximumXYAxis = 2
        x, y = move
        return (minimumXYAxis <= x <= maximumXYAxis) and (minimumXYAxis <= y <= maximumXYAxis)

    # TODO: split verification in more methods, also, clean code
    def moveDidWin(self, shape: MoveShape, move: Move) -> bool:
        x, y = move
        # checking if all row values are same
        if np.all(self.board[y, :] == shape, axis=0):
            return True
        # checking if all column values are same
        if np.all(self.board[:, x] == shape, axis=0):
            return True
        # x == y -> represents primary diagonal coordinates: (0, 0), (1, 1) or (2, 2)
        if x == y and np.all(np.diag(self.board) == shape, axis=0):
            return True
        # x + y = 2 -> represents secondary diagonal coordinates: (0, 2), (1, 1) or (2, 0)
        if (x + y) == 2 and np.all(np.diag(np.fliplr(self.board)) == shape, axis=0):
            return True
        return False

    def reachedMaximumMoves(self) -> bool:
        return len(self.moves) == self.maximumMovesUntilEnd
