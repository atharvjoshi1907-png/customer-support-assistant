import requests

BASE_URL = "http://customer-support-assistant-m7up.onrender.com"


def generate_reply(message):

    response = requests.post(
        f"{BASE_URL}/generate",
        json={"message": message}
    )

    return response.json()