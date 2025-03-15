from datetime import datetime

class User:
    def __init__(self, user_id, name, surname, birthday, password=None, email=None):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.password = password
        self.email = email

    def get_details(self):
        return f"ID: {self.user_id}, Name: {self.name} {self.surname}, Email: {self.email}, Birthday: {self.birthday.strftime('%Y-%m-%d')}"



    def get_age(self):
        today = datetime.now().date()  # Get today's date
        birthday_this_year = self.birthday.replace(year=today.year)  # Set birthday to this year

        # Subtract 1 if the birthday hasn't occurred yet this year
        age = today.year - self.birthday.year - (today < birthday_this_year)

        return age
