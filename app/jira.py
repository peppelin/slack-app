import requests
import json
import os

def create_ticket(user_name, summary):
    token = os.environ['ATLASSIAN_TOKEN']
    username = os.environ['ATLASSIAN_USERNAME']
    url = os.environ['ATLASSIAN_URL'] + '/rest/api/3/issue'
    project_key = "SUP"
    issue_type = "IT Help"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    #auth = (username, token)
    info = {
        "fields": {
            "project":
            {
                "key": project_key
            },
            "summary": summary,
            "issuetype": {
                "name": issue_type
            },
            "reporter": {
                "name": user_name
            }
        }
    }

    r = requests.post(url, headers=headers, auth=(username, token), data=json.dumps(info))
    #print(r.json(), file=sys.stderr)
    return(r.json())
