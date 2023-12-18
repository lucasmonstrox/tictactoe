from src.entities import Game


def test_should_return_True_when_move_coordinate_is_0_0():
    move = (0, 0)
    game = Game()
    assert game.isValidMove(move) == True


def test_should_return_True_when_move_coordinate_is_0_1():
    move = (0, 1)
    game = Game()
    assert game.isValidMove(move) == True


def test_should_return_True_when_move_coordinate_is_0_2():
    move = (0, 2)
    game = Game()
    assert game.isValidMove(move) == True


def test_should_return_True_when_move_coordinate_is_1_0():
    move = (1, 0)
    game = Game()
    assert game.isValidMove(move) == True


def test_should_return_True_when_move_coordinate_is_1_1():
    move = (1, 1)
    game = Game()
    assert game.isValidMove(move) == True


def test_should_return_True_when_move_coordinate_is_1_2():
    move = (1, 2)
    game = Game()
    assert game.isValidMove(move) == True


def test_should_return_True_when_move_coordinate_is_2_0():
    move = (2, 0)
    game = Game()
    assert game.isValidMove(move) == True


def test_should_return_True_when_move_coordinate_is_2_1():
    move = (2, 1)
    game = Game()
    assert game.isValidMove(move) == True


def test_should_return_True_when_move_coordinate_is_2_2():
    move = (2, 2)
    game = Game()
    assert game.isValidMove(move) == True


def test_should_return_False_when_move_coordinate_x_is_lower_than_0():
    move = (-1, 0)
    game = Game()
    assert game.isValidMove(move) == False


def test_should_return_False_when_move_coordinate_x_is_greater_than_2():
    move = (3, 0)
    game = Game()
    assert game.isValidMove(move) == False


def test_should_return_False_when_move_coordinate_y_is_lower_than_0():
    move = (0, -1)
    game = Game()
    assert game.isValidMove(move) == False


def test_should_return_False_when_move_coordinate_y_is_greater_than_2():
    move = (0, 3)
    game = Game()
    assert game.isValidMove(move) == False
