from flask import render_template, request, redirect
from app import app
from models.games import games, new_game
from models.player import *
from models.game import Game


@app.route('/')
def index():
    return render_template('index.html', title='Rock Paper Scissors')


@app.route('/games')
def game_play_index():
    return render_template('games.html', title="Let's Start", games = games)


@app.route('/games', methods=['POST'])
def game_play():
    
    player1 = request.form['player1']
    player2 = request.form['player2']
    player1_choice = request.form['player1_choice']
    player2_choice = request.form['player2_choice']
    newgame = Game(player1 = player1, player2 = player2, player1_choice= player1_choice, player2_choice=player2_choice)
    new_game(newgame)
    return redirect('/games')
