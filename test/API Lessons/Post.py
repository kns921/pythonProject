import requests


class TestNewLocation:

    def test_create_new_location(self):
        base_url = 'https://rahulshettyacademy.com'
        post_resourse = '/maps/api/place/add/json'
        get_resourse = '/maps/api/place/get/json'
        key = '?key=qaclick123'
        post_url = base_url + post_resourse + key
        json_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        print(f'Метод POST. URL: {post_url}\nBody: {json_create_new_location}')

        result_post = requests.post(post_url, json=json_create_new_location)
        print(f'Статус код: {result_post.status_code}, ответ: {result_post.text}')
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print(f'Успех! Статус код корректный: {result_post.status_code}')
        else:
            print('Ошибка! Несовподение статус кода!')
        result_post.encoding = 'utf-8'

        check_result_post = result_post.json()
        check_result_post_info = check_result_post.get('status')
        assert check_result_post_info == 'OK'
        print(f'Статус ответа корректный: {check_result_post_info}')
        place_id = check_result_post.get('place_id')
        print(f'place_id ответа: {place_id}')

        get_url = base_url + get_resourse + key + '&place_id=' + place_id
        print(f'Метод GET. URL: {get_url}\nplace_id: {place_id}')
        result_get = requests.get(get_url)
        print(f'Статус код: {result_get.status_code}, ответ: {result_get.text}')
        assert 200 == result_get.status_code
        if result_post.status_code == 200:
            print(f'Успех! Статус код корректный: {result_get.status_code}')
        else:
            print('Ошибка! Несовподение статус кода!')
        result_post.encoding = 'utf-8'


test_post = TestNewLocation()
test_post.test_create_new_location()
