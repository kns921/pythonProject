from faker import Faker

faker = Faker('ru_RU')

random_name = faker.name()
print(random_name)
