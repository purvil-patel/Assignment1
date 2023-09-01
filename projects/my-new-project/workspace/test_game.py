import pytest
from game import Game

def test_game_start():
    game = Game(800, 600)
    game.start()
    assert game.game_over == True
