import requests

api_base_url = "http://172.17.0.1:8080"


def sendMessageAsUser(user_id, message):
    headers = {'Content-Type': 'application/json'}
    url = api_base_url + "/sendMessage"
    params = {"id": user_id, "message": message, "role": "user"}

    response = requests.post(url=url, headers=headers, params=params)
    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        print(f"Error: {response.status_code}")
        return "ERROR"


def sendMessageAsSystem(user_id, message):
    headers = {'Content-Type': 'application/json'}
    url = api_base_url + "/sendMessage"
    params = {"id": user_id, "message": message, "role": "system"}

    response = requests.post(url=url, headers=headers, params=params)
    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        print(f"Error: {response.status_code}")
        return "ERROR"


def clearMessages(user_id):
    headers = {'Content-Type': 'application/json'}
    url = api_base_url + "/clearMessages"
    params = {"id": user_id}

    response = requests.patch(url=url, headers=headers, params=params)
    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        print(f"Error: {response.status_code}")
        return "ERROR"


def getModel(user_id, message):
    headers = {'Content-Type': 'application/json'}
    url = api_base_url + "/getModel"
    params = {"id": user_id}

    response = requests.get(url=url, headers=headers, params=params)
    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        print(f"Error: {response.status_code}")
        return "ERROR"


def setModel(user_id, model):
    headers = {'Content-Type': 'application/json'}
    url = api_base_url + "/setModel"
    params = {"id": user_id, "model": model}

    response = requests.patch(url=url, headers=headers, params=params)
    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        print(f"Error: {response.status_code}")
        return "ERROR"
