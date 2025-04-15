import requests


class TestNewJoke:
    @staticmethod
    def get_categories():
        # Получаем доступные категории
        url = 'https://api.chucknorris.io/jokes/categories'
        response = requests.get(url)
        response.encoding = 'utf-8'
        assert response.status_code == 200, f'Ошибка! Статус код: {response.status_code}'
        categories = response.json()
        categories_str = ','.join(categories)
        print(f'Доступные категории: {categories_str}')
        return response.json()

    def random_jokes_by_categories(self):
        # Получаем шутку по выбранной категории
        self.get_categories()

        def change_category():
            # Выбор категории с рекурсией при ошибке AssertionError
            print('Выберите категорию')
            category = input()
            url = f'https://api.chucknorris.io/jokes/random?category={category}'
            response = requests.get(url)
            response.encoding = 'utf-8'

            try:
                assert response.status_code == 200
                joke = response.json().get('value')
                print(f'Категория: {category}. Новая шутка: {joke}')
            except AssertionError:
                print('Ошибка! Такой категории не существует, попробуйте еще раз.')
                change_category()

        change_category()


tester = TestNewJoke()
tester.random_jokes_by_categories()
