import requests

BASE_URL = "http://localhost:8000/api"


def request1():
    data = {"username": "kame", "password": "kame"}

    response = requests.post(BASE_URL + "/rest-auth/login/", data=data)

    print("status code", response.status_code)

    print("the responded data is", response.json())


if __name__ == "__main__":
    request1()
