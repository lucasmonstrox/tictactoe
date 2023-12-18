import pytest
from src.entities import Game
from src.errors import Gameover, InvalidMove, MoveIsBusy


def test_should_raise_Gameover_exception_when_game_is_over(mocker):
    game = Game()
    mocker.patch.object(game, 'gameover', return_value=True)
    with pytest.raises(Gameover):
        game.addMove((0, 0))


def test_should_raise_Gameover_exception_when_move_is_not_a_valid_move(mocker):
    game = Game()
    mocker.patch.object(game, 'gameover', return_value=False)
    mocker.patch.object(game, 'isValidMove', return_value=False)
    with pytest.raises(InvalidMove):
        game.addMove((-1, 3))


def test_should_raise_Gameover_exception_when_move_is_not_a_free_move(mocker):
    game = Game()
    game.addMove((0, 0))
    mocker.patch.object(game, 'gameover', return_value=False)
    mocker.patch.object(game, 'isValidMove', return_value=True)
    with pytest.raises(MoveIsBusy):
        game.addMove((0, 0))


def test_should_not_call_moveDidWin_when_has_no_minimum_moves_to_have_winner(mocker):
    game = Game()
    moveDidWinSpy = mocker.spy(game, 'moveDidWin')
    mocker.patch.object(game, 'gameover', return_value=False)
    mocker.patch.object(game, 'isValidMove', return_value=True)
    mocker.patch.object(
        game, 'hasMinimumMovesToHaveWinner', return_value=False)
    game.addMove((0, 0))
    assert moveDidWinSpy.call_count == 0


def test_should_set_result_to_x_when_move_did_win(mocker):
    game = Game()
    reachedMaximumMovesSpy = mocker.spy(game, 'reachedMaximumMoves')
    mocker.patch.object(game, 'gameover', return_value=False)
    mocker.patch.object(game, 'isValidMove', return_value=True)
    mocker.patch.object(
        game, 'hasMinimumMovesToHaveWinner', return_value=True)
    mocker.patch.object(game, 'moveDidWin', return_value=True)
    move = (0, 0)
    game.addMove(move)
    assert game.result == 'x'
    assert reachedMaximumMovesSpy.call_count == 0


def test_should_not_draw(mocker):
    game = Game()
    mocker.patch.object(game, 'gameover', return_value=False)
    mocker.patch.object(game, 'isValidMove', return_value=True)
    mocker.patch.object(
        game, 'hasMinimumMovesToHaveWinner', return_value=True)
    mocker.patch.object(game, 'moveDidWin', return_value=True)
    move = (0, 0)
    game.addMove(move)
    assert game.result == 'x'


def test_should_draw(mocker):
    game = Game()
    mocker.patch.object(game, 'gameover', return_value=False)
    mocker.patch.object(game, 'isValidMove', return_value=True)
    mocker.patch.object(
        game, 'hasMinimumMovesToHaveWinner', return_value=True)
    mocker.patch.object(game, 'moveDidWin', return_value=False)
    mocker.patch.object(game, 'reachedMaximumMoves', return_value=True)
    move = (0, 0)
    game.addMove(move)
    assert game.result == 'draw'
