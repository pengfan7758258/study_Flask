import requests


def get_data():
    url = "http://127.0.0.1:5000/getnewses/"
    resp = requests.get(url)
    print(resp.text)


if __name__ == '__main__':
    get_data()
