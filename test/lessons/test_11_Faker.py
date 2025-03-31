from faker import Faker

faker = Faker('ru_RU')

random_name = faker.name()
random_last_name = faker.last_name()
post = faker.postcode()

print(random_name, post)
