class Persona():
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        print('Персона создана')

    def description_prsson(self):
        description = self.name + ', ему ' + str(self.age) + ', его рост ' + str(self.height) + ', его вес ' + str(
            self.weight)
        print('Новый человек создан: ' + description)

human = Persona('Nikolay', 31, 172, 90)
human.description_prsson()
