# This code sample uses the 'requests' library:
# http://docs.python-requests.org

import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://user-name.atlassian.net/rest/api/3/project"

API_TOKEN="<jira-token>"

auth = HTTPBasicAuth("user-email-id@gmail.com", API_TOKEN)

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
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },    
    "issuetype": {
      "id": "10011"  
    },    
    "project": {
      "key": "VRUS"
    },   
    "summary": "My first jira ticket",    
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

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


######### output ##############
# {
#     "id": "10000",
#     "key": "VRUS-1",
#     "self": "https://vrushaliapotdar.atlassian.net/rest/api/3/issue/10000"
# }