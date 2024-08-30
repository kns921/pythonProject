class Person():
    # модель персоны
    def __init__(self, name, age):
        # инициализация атрибутов: имя возраст
        self.name = name
        self.age = age
        print('Персона создана')

    def sing(self):
        print(self.name + ' поет')

    def dance(self):
        print(self.name + ' танцует')


man = Person('Nik', 31)
woman = Person('Anastasia', 28)
# print(man.name)
man.dance()
woman.sing()
