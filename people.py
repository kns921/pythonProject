# создание персоны
class Person():
    # инициализация атрибутов
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = 70
    # получение описания
    def description(self):
        description = self.name + ', ему ' + str(self.age) + ', его рост ' + str(self.height) + ', его вес ' + str(self.weight)
        print('Новый человек создан: ' + description)
    # получение веса
    def get_weight(self):
        print('Вес человека: ' + str(self.weight))
    # изменение веса
    def update_weight(self, kg):
        self.weight = kg


man = Person('Nikolay', 31, 172, 80)
# man.description()
# man.weight = 120
# man.update_weight(95)
man.get_weight()
