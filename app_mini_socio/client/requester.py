import requests

BASE_URL = "http://localhost:8000/api"


def request1():
    data = {"username": "kame", "password": "kame"}

    response = requests.post(BASE_URL + "/rest-auth/login/", data=data)

    print("status code", response.status_code)

    print("the responded data is", response.json())


def request2():
    token = "Token e70d61107e43de571ce870ddf9a59f849b17144e"
    headers = {"Authorization": token}

    response = requests.get(BASE_URL + "/profiles/", headers=headers)

    print("status code", response.status_code)

    print("the responded data is", response.json())


def request3():
    data = {
        "username": "all_auth_user",
        "email": "one@users.com",
        "password1": "a long password # 23",
        "password2": "a long password # 23",  # confirm password
    }

    response = requests.post(BASE_URL + "/rest-auth/registration", data=data)

    print("status code", response.status_code)

    print("the responded data is", response.json())


if __name__ == "__main__":
    # request1()
    # request2()
    request3()
