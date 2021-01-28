import requests

BASE_URL = "http://localhost:8000/api"


def request1():
    data = {"username": "kame", "password": "kame"}

    response = requests.post(BASE_URL + "/rest-auth/login/", data=data)

    print("status code", response.status_code)

    print("the responded data is", response.json())

def request2():
    token = 'Token e70d61107e43de571ce870ddf9a59f849b17144e'
    headers = {'Authorization':token}

    response = requests.get(BASE_URL+'/profiles/',headers=headers)

    print("status code", response.status_code)

    print("the responded data is", response.json())


if __name__ == "__main__":
    request2()
