from flask import render_template, request, redirect
from app import app
from models.game_play import game_turn, result_match, games, game_turn
from models.player import *
from models.game import Game
from itertools import islice


@app.route('/')
def index():
     return render_template('index.html', title='Rock Paper Scissors')

@app.route('/games')
def game_play_1_page():
     return render_template('game_play.html', title="Let's Start", games=games)

@app.route('/games', methods=['POST'])
def game_play():
    player = request.form['player']
    player_choice = request.form['player_choice']
    game_turn(player, player_choice)
    print(games)
    if len(games) <2:
        return redirect('/games')
    elif len(games) == 2:
        first = list(games.keys())[0]
        second = list(games.keys())[1]
        return result_match(first, second)