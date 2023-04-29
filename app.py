from flask import Flask, request

from api_utils import player_profile

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to a summary of player statistics in the 22/23 NBA season"

@app.route('/players')
def get_player_bio():
    return player_profile()




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)