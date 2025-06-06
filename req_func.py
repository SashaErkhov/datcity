import requests

BASE_URL = "https://games-test.datsteam.dev"
TOKEN = "e7fabef7-8da7-4c3f-8f89-fb40ad4821fc"
headers = {
    "X-Auth-Token": f"{TOKEN}",
    "Content-Type": "application/json"
}

'''
data = {
    "done": False,  # Продолжаем строительство
    "words": [
        {
            "dir": 1,  # Выбор направления
            "id": 123,  # ID слова
            "pos": [0, 0, 0]  # Координаты первой буквы
        },
        {
            "dir": 2,  # Направление [1, 0, 0]
            "id": 124,
            "pos": [1, 0, 0]
        }
    ]
}
'''


def req_words():
    response = requests.get(
        f"{BASE_URL}/api/words",
        headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return False


def req_rounds():
    response = requests.get(
        f"{BASE_URL}/api/rounds",
        headers=headers
    )
    if response.status_code == 200:
        return response.json()
    else:
        return False


def req_towers():
    response = requests.get(
        f"{BASE_URL}/api/towers",
        headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return False

def req_shuffle():
    response = requests.get(
        f"{BASE_URL}/api/shuffle",
        headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return False

def req_build(data):
    response = requests.post(
        f"{BASE_URL}/api/build",
        headers=headers,
        json=data)
    if response.status_code == 404:
        return False
    return response.json()