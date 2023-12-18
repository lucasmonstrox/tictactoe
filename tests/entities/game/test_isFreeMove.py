from src.entities import Game


def test_should_assert_free_moves():
    game = Game()
    assert game.isFreeMove((0, 0)) == True
    assert game.isFreeMove((0, 1)) == True
    assert game.isFreeMove((0, 2)) == True
    assert game.isFreeMove((1, 0)) == True
    assert game.isFreeMove((1, 1)) == True
    assert game.isFreeMove((1, 2)) == True
    assert game.isFreeMove((2, 0)) == True
    assert game.isFreeMove((2, 1)) == True
    assert game.isFreeMove((2, 2)) == True


def test_should_assert_busy_moves():
    game = Game(moves=[
        (0, 0), (1, 0), (2, 0),
        (0, 1), (1, 1), (2, 1),
        (1, 2), (0, 2), (2, 2),
    ])
    assert game.isFreeMove((0, 0)) == False
    assert game.isFreeMove((1, 0)) == False
    assert game.isFreeMove((2, 0)) == False
    assert game.isFreeMove((0, 1)) == False
    assert game.isFreeMove((1, 1)) == False
    assert game.isFreeMove((2, 1)) == False
    assert game.isFreeMove((1, 2)) == False
    assert game.isFreeMove((0, 2)) == False
    assert game.isFreeMove((2, 2)) == False
