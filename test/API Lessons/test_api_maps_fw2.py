import requests


class TestNewLocation:

    def test_create_new_location(self):
        base_url = 'https://rahulshettyacademy.com'
        # Эндпоинты
        get_resourse = '/maps/api/place/get/json'
        delete_resourse = '/maps/api/place/delete/json'
        key = '?key=qaclick123'

        """Чтение place_id из файла"""
        fw = open('../files/place_id.txt', 'r')
        file_place_id = [line.strip() for line in fw if line.strip()]
        fw.close()

        """Метод DELETE — удаление 2-й и 4-й локации"""
        delete_url = base_url + delete_resourse + key
        for index in [1, 3]:  # 2-й и 4-й элемент
            delete_id = file_place_id[index]

            json_delete_location = {
                "place_id": delete_id
            }

            result_delete = requests.delete(delete_url, json=json_delete_location)
            print(f'Метод DELETE. URL: {delete_url},\nplace_id: {delete_id},\nBody: {json_delete_location}')
            print(f'Статус код: {result_delete.status_code}, ответ: {result_delete.text}')

            assert result_delete.status_code == 200
            result_delete = result_delete.json()
            check_result_delete_info = result_delete.get('status')
            assert check_result_delete_info == "OK"
            print(f'Статус ответа корректный: {check_result_delete_info}')

        """Метод GET — проверка актуальных и неактуальных"""
        get_url_half = base_url + get_resourse + key
        actual_id = []

        for place_id in file_place_id:
            get_url_full = get_url_half + '&place_id=' + place_id
            result_get = requests.get(get_url_full)
            print(f'Метод GET. URL: {get_url_full}')
            print(f'Статус код: {result_get.status_code}, ответ: {result_get.text}')

            if result_get.status_code == 200:
                print(f'Успех! Локация существует. Статус код: {result_get.status_code}')
                actual_id.append(place_id)
            else:
                print(f'Локация НЕ найдена (возможно удалена). Код: {result_get.status_code}')

        """Запись актуальных place_id в новый файл"""
        fw = open('../files/actual_place_id.txt', 'w')
        for place_id in actual_id:
            fw.write(place_id + '\n')
        fw.close()
        print('Cоздан файл actual_place_id.txt с актуальными place_id.')


test_post = TestNewLocation()
test_post.test_create_new_location()
