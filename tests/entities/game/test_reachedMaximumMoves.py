from src.entities import Game


def test_should_return_False_when_didnt_reached_maximum_moves():
    game = Game()
    assert game.reachedMaximumMoves() == False


def test_should_return_True_when_reached_maximum_moves():
    game = Game(moves=[
                (0, 0), (1, 0), (2, 0),
                (0, 1), (1, 1), (2, 1),
                (1, 2), (0, 2), (2, 2),
                ])
    assert game.reachedMaximumMoves() == True
