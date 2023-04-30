from flask import Flask

from api_utils import player_profile, player_profiles_by_id

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to a summary of player statistics in the 22/23 NBA season"

@app.route('/players')
def get_player_bio():
    return player_profile()

@app.route('/players/<player_id>')
def player_bio_by_id(player_id):
    list_of_ids = player_id.split(',')
    return player_profiles_by_id(list_of_ids)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)