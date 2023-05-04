from flask import Flask

from api_utils import (delete_players, player_profiles, player_profiles_by_id,
                       players_defense, players_offense)

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to a summary of player statistics in the 22/23 NBA season"

@app.route('/players')
def get_player_bio():
    return player_profiles

@app.route('/players/<player_id>')
def player_bio_by_id(player_id):
    list_of_ids = player_id.split(',')
    return player_profiles_by_id(list_of_ids)

@app.route('/players/<player_id>', methods = ['DELETE'])
def remove_player_by_id(player_id):
    list_of_ids = player_id.split(',')
    return delete_players(list_of_ids)

@app.route('/offense')
def get_attacking_stats():
    return players_offense

@app.route('/defense')
def get_defensive_stats():
    return players_defense

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)