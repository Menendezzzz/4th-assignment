import random
from datetime import datetime
import re

class UserUtil:
    @staticmethod
    def generate_user_id():
        year_prefix = str(datetime.now().year)[-2:]
        random_suffix = ''.join(random.choices("0123456789", k=7))
        return int(year_prefix + random_suffix)

    @staticmethod
    def generate_password():
        import string
        chars = string.ascii_letters + string.digits + "!@#$%^&*()"
        while True:
            password = ''.join(random.choices(chars, k=8))
            if UserUtil.is_strong_password(password):
                return password

    @staticmethod
    def is_strong_password(password):
        return (len(password) >= 8 and
                any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in "!@#$%^&*()" for c in password))

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        pattern = r'^[a-z]+\.[a-z]+@[a-z]+\.[a-z]+$'
        return re.match(pattern, email) is not None

