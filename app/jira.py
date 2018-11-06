import requests
import json
import os


#===========================
# We get the Jira URL and use a specific user and token to open ticket to the given project.
# You can change it in the project_key and issue_type vars
#===========================
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
    #========
    # Print flask output for debugging purposes
    #========
    #print(r.json(), file=sys.stderr)
    return(r.json())
