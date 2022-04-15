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
def game_play_1():
    player1 = request.form['player1']
    player1_choice = request.form['player1_choice']
    game_turn(player1, player1_choice)
    print(games)
    if len(games) <2:
        return redirect('/games')
    elif len(games) == 2:
        first = list(games.values())[0]
        second = list(games.values())[1]
        return result_match(first, second)
    else:
        return redirect('/')
    

# @app.route('/games2')
# def game_play_2_page():
#     return render_template('game_play2.html', title="Let's Start", games=games)

# @app.route('/games2', methods=['POST'])
# def game_play_2():
#     player2 = request.form['player2']
#     player2_choice = request.form['player2_choice']
#     game_turn(player2, player2_choice)
    
