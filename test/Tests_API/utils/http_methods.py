import requests


class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def post(url):
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def put(url):
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def delete(url):
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result
