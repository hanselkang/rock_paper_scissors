from models.player import Player
from models.game import Game

games = {}

def game_turn(player, choice):
    games[player]=choice


def result_match(name1,name2):
    if games[name1] == games[name2]:
        return "Draw"
