from src.entities import Game


def test_should_return_x_when_previous_move_is_o():
    game = Game()
    assert game.getNextMoveShape() == 'x'


def test_should_return_o_when_previous_move_is_x():
    game = Game()
    game.currentMoveShape = 'x'
    assert game.getNextMoveShape() == 'o'
