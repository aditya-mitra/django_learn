import requests

def main():
    response = requests.get('https://www.googleapis.com/books/v1/volumes',params={'q':'isbn:0747532699'})
    
    if response.status_code != 200:
        print(response.status_code)
        raise Exception('got 200 error')

    print('got the response as', response.json())
    
if __name__ == '__main__':
    main()