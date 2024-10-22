from faker import Faker

fake = Faker("ru_RU")
PAYLOAD_FOR_USER = {"email": fake.email(),
                    "password": fake.password(),
                    "name": fake.name()
                    }
