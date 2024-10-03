from faker import Faker
from urls import Endpoints
import requests
import random

faker = Faker()
fakeRU = Faker(locale='ru_RU')


class RegisterNewUser:

    @staticmethod
    def generate_new_user_data():
        name = faker.first_name()
        email = faker.free_email()
        password = faker.password(length=10, special_chars=False, digits=False, upper_case=False, lower_case=True)

        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload


def get_order_data():
    response = requests.get(Endpoints.INGREDIENTS)
    ingredients_data = response.json().get('data', [])

    categories = {'bun': [], 'main': [], 'sauce': []}

    for ingredient in ingredients_data:
        category = ingredient.get('type')
        if category in categories:
            categories[category].append(ingredient['_id'])

    selected_ingredients = [
        random.choice(categories['bun']),
        random.choice(categories['main']),
        random.choice(categories['sauce'])
    ]

    return selected_ingredients
