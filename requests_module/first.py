import requests


def main():
    response = requests.get("https://aditya-mitra.netlify.app")
    print(response.headers, response.status_code)


if __name__ == "__main__":
    main()
