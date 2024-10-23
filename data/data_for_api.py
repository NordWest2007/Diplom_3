from faker import Faker

fake = Faker("ru_RU")


class DataApi:
    PAYLOAD_FOR_USER = {"email": fake.email(),
                        "password": fake.password(),
                        "name": fake.name()
                        }
    BASE_ENDPOINT = 'https://stellarburgers.nomoreparties.site'
    ENDPOINT_CREATE_USER = f'{BASE_ENDPOINT}/api/auth/register'
    ENDPOINT_LOGIN = f'{BASE_ENDPOINT}/api/auth/login'
    ENDPOINT_DELETE = f'{BASE_ENDPOINT}/api/auth/user'
