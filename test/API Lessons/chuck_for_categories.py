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
        print(f'Доступные категории: {categories}')
        return response.json()

    def random_jokes_by_categories(self):
        # Получаем новые шутки по кажной из доступной категории
        categories = self.get_categories()
        # print(categories)
        for category in categories:
            url = f'https://api.chucknorris.io/jokes/random?category={category}'
            response = requests.get(url)
            response.encoding = 'utf-8'
            assert response.status_code == 200, f'Ошибка! Статус код: {response.status_code} для категории {category}'
            joke = response.json().get('value')
            print(f'Категория: {category}. Новая шутка: {joke}')


tester = TestNewJoke()
tester.random_jokes_by_categories()
