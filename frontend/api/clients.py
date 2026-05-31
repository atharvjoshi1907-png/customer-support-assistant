import requests

BASE_URL = "http://127.0.0.1:5000"


def generate_reply(message):

    response = requests.post(
        f"{BASE_URL}/generate",
        json={"message": message}
    )

    return response.json()