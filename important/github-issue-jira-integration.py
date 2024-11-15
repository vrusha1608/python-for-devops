from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json


# 1. Create a github webhook
# 2. Python-for-devops repository -> Settings -> Webhook -> Add Webhook
# 3. Payload URL = http://<public-ip-ec2-instance>:5000/createJira
# 4. Content type = application/json
# 5. Select Individual Event = Issue comments, push

# create flask app instance
app = Flask(__name__)

# Define a route that handles HTTP requests
@app.route("/createJira", methods=['POST'])
def createJira():
    url = "https://[jira-user-domain].atlassian.net/rest/api/3/issue"

    API_TOKEN="jira-token"

    auth = HTTPBasicAuth("<jira-user-email>@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "VRUS"
        },
        "issuetype": {
            "id": "10006"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )


    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0', port=5000)