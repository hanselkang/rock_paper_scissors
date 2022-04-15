from models.player import Player
from models.game import Game

player1_score = 0
player2_score = 0
games = {}


def result_route(player1, player2):

    if player1 == player2:
        return "Draw"
    elif player1 == "Rock" and player2 == "Scissors":
        return " Player1 wins by playing " + player1
    elif player1 == "Scissors" and player2 == "Paper":
        return " Player1 wins by playing " + player1
    elif player1 == "Paper" and player2 == "Rock":
        return " Player1 wins by playing " + player1

    return " Player2 wins by playing " + player2


def game_turn(player, choice):
    games[player] = choice


def result_match(name1, name2):

    if games[name1] == games[name2]:
        return "Draw"
    elif games[name1] == "Rock" and games[name2] == "Scissors":
        return list(games.keys())[0] + " wins by playing " + games[name1]
    elif games[name1] == "Scissors" and games[name2] == "Paper":
        return list(games.keys())[0] + " wins by playing " + games[name1]
    elif games[name1] == "Paper" and games[name2] == "Rock":
        return list(games.keys())[0] + " wins by playing " + games[name1]

    return list(games.keys())[1] + " wins by playing " + games[name2]



def empty_dict(dict):
    return dict.clear()
