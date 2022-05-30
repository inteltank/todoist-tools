import requests, os

TODOIST_API_URL = "https://api.todoist.com/rest/v1/tasks"
API_TOKEN = os.environ["TODOIST_API_TOKEN"] 

headers = {
        "Authorization": "Bearer {}".format(API_TOKEN)
        }
response = requests.get(TODOIST_API_URL,headers=headers)
print(response.text)
