from faker import Faker

fake = Faker()

def generate_user():
    return {
        "email": fake.email(),
        "username": fake.user_name(),
        "password": fake.password()
    }
