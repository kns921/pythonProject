class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        # print('Персона создана')

    def description_prsson(self):
        description = self.name + ', ему ' + str(self.age) + ', его рост ' + str(self.height) + ', его вес ' + str(
            self.weight)
        print('Новый человек создан: ' + description)

    def get_weight(self):
        print('Вес человека: ', str(self.weight))

    def weight_update(self):
        self.weight = 'kg'


class Warrior(Person):
    # создали класс воина
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)
        self.rage = 100
        # инициализировали атрибуты класса

    def get_rage(self):
        print('Заряд ярости равен: ' + str(self.rage))

    def description_warrior(self):
        description = self.name + ', его вес ' + str(self.weight) + ', его заряд ярости ' + str(self.rage)
        print('Новый воин создан: ' + description)
        # return description


# human = Person('Nikolay', 31, 172, 90)
# human.description_prsson()
# warrior = Warrior('Ahawe', 34, 170, 75)
# warrior.description_warrior()
