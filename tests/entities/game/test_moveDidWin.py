import numpy as np
from src.entities import Game


def test_should_return_True_when_last_move_did_win_in_first_row_at_0_0():
    game = Game()
    game.board = np.array([
        ['x', 'x', 'x'],
        ['', '', ''],
        ['', '', '']
    ])
    assert game.moveDidWin('x', (0, 0)) == True


def test_should_return_True_when_last_move_did_win_in_first_row_at_1_0():
    game = Game()
    game.board = np.array([
        ['x', 'x', 'x'],
        ['', '', ''],
        ['', '', '']
    ])
    assert game.moveDidWin('x', (1, 0)) == True


def test_should_return_True_when_last_move_did_win_in_first_row_at_2_0():
    game = Game()
    game.board = np.array([
        ['x', 'x', 'x'],
        ['', '', ''],
        ['', '', '']
    ])
    assert game.moveDidWin('x', (2, 0)) == True


def test_should_return_True_when_last_move_did_win_in_second_row_at_0_1():
    game = Game()
    game.board = np.array([
        ['', '', ''],
        ['x', 'x', 'x'],
        ['', '', '']
    ])
    assert game.moveDidWin('x', (0, 1)) == True


def test_should_return_True_when_last_move_did_win_in_second_row_at_1_1():
    game = Game()
    game.board = np.array([
        ['', '', ''],
        ['x', 'x', 'x'],
        ['', '', '']
    ])
    assert game.moveDidWin('x', (1, 1)) == True


def test_should_return_True_when_last_move_did_win_in_second_row_at_2_1():
    game = Game()
    game.board = np.array([
        ['', '', ''],
        ['x', 'x', 'x'],
        ['', '', '']
    ])
    assert game.moveDidWin('x', (2, 1)) == True


def test_should_return_True_when_last_move_did_win_in_third_row_at_0_2():
    game = Game()
    game.board = np.array([
        ['', '', ''],
        ['', '', ''],
        ['x', 'x', 'x']
    ])
    assert game.moveDidWin('x', (0, 2)) == True


def test_should_return_True_when_last_move_did_win_in_third_row_at_1_2():
    game = Game()
    game.board = np.array([
        ['', '', ''],
        ['', '', ''],
        ['x', 'x', 'x']
    ])
    assert game.moveDidWin('x', (1, 2)) == True


def test_should_return_True_when_last_move_did_win_in_third_row_at_2_2():
    game = Game()
    game.board = np.array([
        ['', '', ''],
        ['', '', ''],
        ['x', 'x', 'x']
    ])
    assert game.moveDidWin('x', (2, 2)) == True


def test_should_return_True_when_last_move_did_win_in_first_column_at_0_0():
    game = Game()
    game.board = np.array([
        ['x', '', ''],
        ['x', '', ''],
        ['x', '', '']
    ])
    assert game.moveDidWin('x', (0, 0)) == True


def test_should_return_True_when_last_move_did_win_in_first_column_at_0_1():
    game = Game()
    game.board = np.array([
        ['x', '', ''],
        ['x', '', ''],
        ['x', '', '']
    ])
    assert game.moveDidWin('x', (0, 1)) == True


def test_should_return_True_when_last_move_did_win_in_first_column_at_0_2():
    game = Game()
    game.board = np.array([
        ['x', '', ''],
        ['x', '', ''],
        ['x', '', '']
    ])
    assert game.moveDidWin('x', (0, 2)) == True


def test_should_return_True_when_last_move_did_win_in_second_column_at_1_0():
    game = Game()
    game.board = np.array([
        ['', 'x', ''],
        ['', 'x', ''],
        ['', 'x', '']
    ])
    assert game.moveDidWin('x', (1, 0)) == True


def test_should_return_True_when_last_move_did_win_in_second_column_at_1_1():
    game = Game()
    game.board = np.array([
        ['', 'x', ''],
        ['', 'x', ''],
        ['', 'x', '']
    ])
    assert game.moveDidWin('x', (1, 1)) == True


def test_should_return_True_when_last_move_did_win_in_second_column_at_1_2():
    game = Game()
    game.board = np.array([
        ['', 'x', ''],
        ['', 'x', ''],
        ['', 'x', '']
    ])
    assert game.moveDidWin('x', (1, 2)) == True


def test_should_return_True_when_last_move_did_win_in_third_column_at_2_0():
    game = Game()
    game.board = np.array([
        ['', '', 'x'],
        ['', '', 'x'],
        ['', '', 'x']
    ])
    assert game.moveDidWin('x', (2, 0)) == True


def test_should_return_True_when_last_move_did_win_in_third_column_at_2_1():
    game = Game()
    game.board = np.array([
        ['', '', 'x'],
        ['', '', 'x'],
        ['', '', 'x']
    ])
    assert game.moveDidWin('x', (2, 1)) == True


def test_should_return_True_when_last_move_did_win_in_third_column_at_2_2():
    game = Game()
    game.board = np.array([
        ['', '', 'x'],
        ['', '', 'x'],
        ['', '', 'x']
    ])
    assert game.moveDidWin('x', (2, 2)) == True


def test_should_return_True_when_last_move_did_win_in_diagonal_at_0_0():
    game = Game()
    game.board = np.array([
        ['x', '', ''],
        ['', 'x', ''],
        ['', '', 'x']
    ])
    assert game.moveDidWin('x', (0, 0)) == True


def test_should_return_True_when_last_move_did_win_in_diagonal_at_1_1():
    game = Game()
    game.board = np.array([
        ['x', '', ''],
        ['', 'x', ''],
        ['', '', 'x']
    ])
    assert game.moveDidWin('x', (1, 1)) == True


def test_should_return_True_when_last_move_did_win_in_diagonal_at_2_2():
    game = Game()
    game.board = np.array([
        ['x', '', ''],
        ['', 'x', ''],
        ['', '', 'x']
    ])
    assert game.moveDidWin('x', (2, 2)) == True


def test_should_return_True_when_last_move_did_win_in_secondary_diagonal_at_2_0():
    game = Game()
    game.board = np.array([
        ['', '', 'x'],
        ['', 'x', ''],
        ['x', '', '']
    ])
    assert game.moveDidWin('x', (2, 0)) == True


def test_should_return_True_when_last_move_did_win_in_secondary_diagonal_at_1_1():
    game = Game()
    game.board = np.array([
        ['', '', 'x'],
        ['', 'x', ''],
        ['x', '', '']
    ])
    assert game.moveDidWin('x', (1, 1)) == True


def test_should_return_True_when_last_move_did_win_in_secondary_diagonal_at_0_2():
    game = Game()
    game.board = np.array([
        ['', '', 'x'],
        ['', 'x', ''],
        ['x', '', '']
    ])
    assert game.moveDidWin('x', (0, 2)) == True
