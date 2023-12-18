from src.entities import Game


def test_should_return_False_when_there_is_no_moves():
    game = Game()
    assert game.hasMinimumMovesToHaveWinner() == False


def test_should_return_False_when_there_is_one_move():
    moves = [(0, 0)]
    game = Game(moves=moves)
    assert game.hasMinimumMovesToHaveWinner() == False


def test_should_return_False_when_there_is_two_moves():
    moves = [(0, 0), (0, 1)]
    game = Game(moves=moves)
    assert game.hasMinimumMovesToHaveWinner() == False


def test_should_return_False_when_there_is_three_moves():
    moves = [(0, 0), (1, 0), (0, 1)]
    game = Game(moves=moves)
    assert game.hasMinimumMovesToHaveWinner() == False


def test_should_return_False_when_there_is_four_moves():
    moves = [(0, 0), (1, 0), (0, 1), (1, 1)]
    game = Game(moves=moves)
    assert game.hasMinimumMovesToHaveWinner() == False


def test_should_return_True_when_there_is_at_least_5_moves():
    moves = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)]
    game = Game(moves=moves)
    assert game.hasMinimumMovesToHaveWinner() == True
