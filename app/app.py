from flask import Flask, request, jsonify
import subprocess
import jira

app = Flask(__name__)


# List of allowed channels to use the commands
allowed_channels = {'test'}


def granted_channel(channel):
    return channel in allowed_channels

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/message', methods=['POST'])
def hello_name():
    text = request.form["text"]
    return "*" + text + "*" + request.form["user_name"]


@app.route('/ticket', methods=['POST'])
def ticket():
    slack_event = request.form
    if granted_channel(slack_event['channel_name']):
        user_name = slack_event["user_name"]
        command_raw = slack_event['text'].split('"')
        issue_type = command_raw[1]
        summary = command_raw[3]
        ticket = jira.create_ticket(user_name, summary, issue_type)
        return ticket
    else:
        return 'You are not allowed to use commands'


@app.route('/command', methods=['POST'])
def execute_command():
    slack_event = request.form
    if granted_channel(slack_event['channel_name']):
        command_raw = slack_event['text'].split()
        command = command_raw[0]
        args = ' '.join(str(item) for item in command_raw[1:])
        process = subprocess.Popen([command, args], stdout=subprocess.PIPE, universal_newlines=True)
        output = ''
        for line in process.stdout:
            output = output + line
        return command + ' ' + args + '\n' + output.rstrip('\n')
    else:
        return 'You are not allowed to use commands'


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
        return make_response(slack_event["challenge"], 200, {"content_type":"application/json"})

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
