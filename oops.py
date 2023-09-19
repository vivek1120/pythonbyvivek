from datetime import date
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth
        return age
    


inst = Person("vivek","india",date(2002,12,31))

print(inst.calculate_age())