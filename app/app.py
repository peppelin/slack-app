from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/message', methods=['POST'])
def hello_name():
    text = request.form["text"]
    return "*" + text + "*"

@app.route('/test', methods=['POST'])
def send_button():
    payload = {
        "text": "Would you like to play a game?",
        "attachments": 
        [{
            "text": "Choose a game to play",
            "fallback": "You are unable to choose a game",
            "callback_id": "wopr_game",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "actions":
            [{
                "name": "game",
                "text": "Chess",
                "type": "button",
                "value": "chess"
            },
            {
                "name": "game",
                "text": "Falken's Maze",
                "type": "button",
                "value": "maze"
            },
            {
                "name": "game",
                "text": "Thermonuclear War",
                "style": "danger",
                "type": "button",
                "value": "war",
                "confirm": 
                {
                    "title": "Are you sure?",
                    "text": "Wouldn't you prefer a good game of chess?",
                    "ok_text": "Yes",
                    "dismiss_text": "No"
                }
            }]
        }]
    }
    return jsonify(text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
