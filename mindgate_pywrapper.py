import requests

api_base_url = "http://localhost:8080"


def sendMessageAsUser(user_id, message):
    headers = {'Content-Type': 'application/json'}
    url = api_base_url + "/sendMessage"
    params = {"id": user_id, "message": message, "role": "user"}

    response = requests.post(url=url, headers=headers, params=params)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        return "ERROR"


def sendMessageAsSystem(user_id, message):
    headers = {'Content-Type': 'application/json'}
    url = api_base_url + "/sendMessage"
    params = {"id": user_id, "message": message, "role": "system"}

    response = requests.post(url=url, headers=headers, params=params)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        return "ERROR"


def clearMessages(user_id):
    headers = {'Content-Type': 'application/json'}
    url = api_base_url + "/clearMessages"
    params = {"id": user_id}

    response = requests.patch(url=url, headers=headers, params=params)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        return "ERROR"
