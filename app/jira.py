import requests
import json


url = "https://mediastreamag.atlassian.net/rest/api/3/issue"
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json",
   "Bearer": "pDPZoHFoeRIGpStHCBALCC16"
}

def create_ticket(user_name, description, issue_type):
    url = "https://mediastreamag.atlassian.net/rest/api/3/issue"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Bearer": "pDPZoHFoeRIGpStHCBALCC16"
    }
    info = {
        "fields": {
            "project":
            {
                "key": "MT"
            },
            "summary": "REST ye merry gentlemen.",
            "description": "Creating of an issue using project keys and issue type names using the REST API",
            "issuetype": {
                "name": "Bug"
            },
            "reporter": {
                "name": user_name
            }
        }
    }

    r = requests.request('POST', url, headers=json.dumps(headers),  data=info)
    print(r.content)
    return("hola")
