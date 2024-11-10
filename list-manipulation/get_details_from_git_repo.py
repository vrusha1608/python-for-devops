# Get pull requests information from a github repo

import requests

response = requests.get("https://api.github.com/repos/vrusha1608/python-for-devops")

# Google => https://api.github.com/repos/vrusha1608/python-for-devops => u will get json output of url

# print(response)
# print(type(response))
# print(response.json())
# print(response.status_code)

all_detail = response.json()

print("full_name ==>",all_detail["full_name"])
print("owner's login ==>",all_detail["owner"]["login"])
print("description ==>",all_detail["description"])
print("updated at ==>",all_detail["updated_at"])
print("created at ==>",all_detail["created_at"])


#  To get pull requests information from a github repo
# response = requests.get("https://api.github.com/repos/vrusha1608/python-for-devops/pulls")
# all_detail = response.json()
# for i in range(len(all_detail)):
#     print(all_detail[i]["user"]["login"])