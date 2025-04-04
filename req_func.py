import requests

BASE_URL = "https://games-test.datsteam.dev"
TOKEN = "e7fabef7-8da7-4c3f-8f89-fb40ad4821fc"
headers = {
    "X-Auth-Token": f"{TOKEN}",
    "Content-Type": "application/json"
}


def req_words():
    response = requests.get(
        f"{BASE_URL}/api/words",
        headers=headers)
    b = response.json()
    return b['words']


def req_rounds():
    response = requests.get(
        f"{BASE_URL}/api/rounds",
        headers=headers
    )
    return response.json()



def req_towers():
    response = requests.get(
        f"{BASE_URL}/api/towers",
        headers=headers)
    return response.json()

def egor():
    pass
