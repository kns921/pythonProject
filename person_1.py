class Person():
    # модель персоны
    def __init__(self, name, age, height, weight):
        # инициализация атрибутов: имя возраст
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        # print('Персона создана')
    def description(self):
        description = self.name + ', ему ' + str(self.age) + ', его рост ' + str(self.height) + ', его вес ' + str(
            self.weight)
        print('Новый человек создан: ' + description)
    def sing(self):
        print(self.name + ' поет')
    def dance(self):
        print(self.name + ' танцует')

# man = Person('Nik', 31, 172, 80)
# woman = Person('Anastasia', 28, 156, 50)
# print(man.name)
# man.dance()
# woman.sing()

class Warrior(Person):
    # создали класс воина
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)
        # инициализировали атрибуты класса
warrior = Warrior('Konan', 31, 210, 130)
warrior.description()

man = Person('Anakoliy', 31, 172, 90)
man.description()

woman = Person('Anastasia', 28, 156, 50)
woman.description()

# 8:34
# https://stepik.org/lesson/740328/step/1?unit=741998