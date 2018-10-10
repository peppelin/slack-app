from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/message', methods=['POST'])
def hello_name():
    text = request.form['text']
    return 'Now it\'s bold! *' + text + '*'


@app.route('/command', methods=['POST'])
def execute_command():
    command = request.form['text']
    process = subprocess.Popen(['ls', command], stdout=subprocess.PIPE, universal_newlines=True)
    output = process.stdout.readline()
    return '*' + output + '*'


@app.route('/listening', methods=['POST'])
# ================================================= #
#    This route listens for incoming events from Slack and uses the event
#    handler helper function to route events to our Bot.
# ================================================= #
def hears():
    slack_event = request.get_json()
    # ============= Slack URL Verification ============ #
    # In order to verify the url of our endpoint, Slack will send a challenge
    # token in a request and check for this token in the response our endpoint
    # sends back.
    #       For more info: https://api.slack.com/events/url_verification
    # ================================================= #
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})


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
    return jsonify(payload)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
