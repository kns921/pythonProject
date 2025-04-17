import requests


class TestNewLocation:

    def test_create_new_location(self):
        # Файл для сохранения place_id
        fw = open('../files/place_id.txt', 'a')

        base_url = 'https://rahulshettyacademy.com'
        # Эндпоинты
        post_resourse = '/maps/api/place/add/json'
        get_resourse = '/maps/api/place/get/json'
        put_resourse = '/maps/api/place/update/json'
        delete_resourse = '/maps/api/place/delete/json'
        key = '?key=qaclick123'

        """Метод POST Создание новой локации"""

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

        # Сохранение place_id в файл
        fw.write(place_id + '\n')
        fw.close()
        print('Place_id сохранен')

        """Метод GET Получение созданной локации"""

        # Чтение файла и сохранение place_id в переменную last_id
        fw = open('../files/place_id.txt', 'r')
        last_id = fw.readlines()[-1].strip()
        fw.close()

        get_url = base_url + get_resourse + key + '&place_id=' + last_id
        print(f'Метод GET. URL: {get_url}\nplace_id: {last_id}')
        result_get = requests.get(get_url)
        print(f'Статус код: {result_get.status_code}, ответ: {result_get.text}')
        assert 200 == result_get.status_code
        if result_post.status_code == 200:
            print(f'Успех! Статус код корректный: {result_get.status_code}')
        else:
            print('Ошибка! Несовподение статус кода!')
        result_post.encoding = 'utf-8'

        """Метод PUT Изменение созданной локации"""

        put_url = base_url + put_resourse + key
        json_update_location = {
            "place_id": last_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json=json_update_location)
        print(f'Метод PUT. URL: {put_url},\nplace_id: {last_id},\nBody: {json_update_location}')
        print(f'Статус код: {result_put.status_code}, ответ: {result_put.text}')
        assert 200 == result_put.status_code
        if result_put.status_code == 200:
            print(f'Успех! Статус код корректный: {result_put.status_code}')
        else:
            print('Ошибка! Несовподение статус кода!')
        check_result_put = result_put.json()
        check_result_put_info = check_result_put.get('msg')
        assert check_result_put_info == 'Address successfully updated'
        print(f'Статус ответа корректный: {check_result_put_info}')

        # Fake place_id 404

        json_fake_update_location = {
            "place_id": "55555555",
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        fake_put = requests.put(put_url, json=json_update_location)
        print(f'Метод PUT. URL: {put_url},\nplace_id: {last_id},\nBody: {json_fake_update_location}')
        print(f'Статус код: {fake_put.status_code}, ответ: {fake_put.text}')
        assert 404 == fake_put.status_code
        if fake_put.status_code == 404:
            print(f'Успех! Статус код корректный: {fake_put.status_code}')
        else:
            print('Ошибка! Несовподение статус кода!')
        check_fake_result_put = fake_put.json()
        check_result_fake_put_info = check_fake_result_put.get('msg')
        assert check_result_fake_put_info == "Update address operation failed, looks like the data doesn't exists"
        print(f'Статус ответа корректный: {check_result_fake_put_info}')

        """Метод DELETE Удаление созданной локации"""

        delete_url = base_url + delete_resourse + key
        json_delete_location = {
            "place_id": last_id
        }
        result_delete = requests.delete(delete_url, json=json_delete_location)
        print(f'Метод DELETE. URL: {result_delete},\nplace_id: {last_id},\nBody: {json_delete_location}')
        print(f'Статус код: {result_delete.status_code}, ответ: {result_delete.text}')
        assert result_delete.status_code == 200
        if result_delete.status_code == 200:
            print(f'Успех! Статус код корректный: {result_delete.status_code}')
        else:
            print('Ошибка! Несовподение статус кода!')
        result_delete = result_delete.json()
        check_result_delete_info = result_delete.get('status')
        assert check_result_delete_info == "OK"
        print(f'Статус ответа корректный: {check_result_delete_info}')
        result_post.encoding = 'utf-8'


test_post = TestNewLocation()
# Вызываем функцию через цикл 5 раз
for i in range(5):
    test_post.test_create_new_location()
