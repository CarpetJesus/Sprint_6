from faker import Faker
import random
from datetime import datetime, timedelta

faker = Faker('ru_RU')

def generate_order_data():
    name = faker.first_name()
    last_name = faker.last_name()
    address = faker.street_name()
    phone = "8" + "".join(str(random.randint(0, 9)) for _ in range(10))
    delivery_date = (datetime.now() + timedelta(days=random.randint(1, 5))).strftime("%d.%m.%Y")
    comment = faker.sentence(nb_words=6)

    return {
        "name": name,
        "last_name": last_name,
        "address": address,
        "phone": phone,
        "delivery_date": delivery_date,
        "comment": comment
    }
