from models.game import *

game1 = Game("Hansel", "Aelish", "Rock", "Paper")

games = [game1]


def new_game(game):
    games.append(game)
