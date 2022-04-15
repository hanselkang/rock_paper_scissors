from models.player import Player
from models.game import Game

games = {}

def game_turn(player, choice):
    games[player]=choice


def result_match(name1,name2):

    if games[name1] == games[name2]:
        return "Draw"
    elif games[name1] == "Rock" and games[name2] == "Scissors":
        return list(games.keys())[0] + " wins by playing " + games[name1]
    elif games[name1] == "Scissors" and games[name2] == "Paper":
        return list(games.keys())[0] + " wins by playing " + games[name1]
    elif games[name1] == "Paper" and games[name2] == "Rock":
        return list(games.keys())[0] + " wins by playing " + games[name1]

    return list(games.keys())[1] + " wins by playing " + games[name2]