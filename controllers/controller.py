from flask import render_template, request, redirect
from app import app
from models.game_play import empty_dict, game_turn, result_match, games, game_turn, result_route, single_game_turn, single_games, single_result_match, empty_dict_single
from models.player import *
from models.game import Game

@app.route('/<player1>/<player2>')
def game(player1, player2):
    return result_route(player1,player2)


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

    if len(games) < 2:
        return redirect('/games')
    elif len(games) == 2:
        first = list(games.keys())[0]
        second = list(games.keys())[1]
        result_match(first, second)
        return render_template('game_result.html', title="Result", games=games, a=result_match(first, second), b=empty_dict(games))


@app.route('/single_game')
def game_play_2_page():
    return render_template('single_play.html', title="Let's Start", single_games=single_games)

@app.route('/single_game', methods=['POST'])
def single_play():
    player = request.form['player']
    player_choice = request.form['player_choice']
    single_game_turn(player, player_choice)
    first = list(single_games.keys())[1]
    single_result_match(first)
    return render_template('game_result.html', title="Result", single_games=single_games, a=single_result_match(first), b=empty_dict_single(single_games))
    

       
