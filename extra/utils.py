from faker import Faker
fake = Faker(['ru_RU'])


def generate_firstname():
    return fake.first_name()


def generate_lastname():
    return fake.last_name()


def generate_email():
    return fake.email()


def generate_phone():
    return fake.phone_number()


def generate_password():
    return fake.password()


def generate_text():
    return fake.text(30)
