class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, 2023 - year)


    @staticmethod
    def is_adult(age):
        return age >= 18


person1 = Person.from_birth_year('Zahid', 1997)
person2 = Person('Anu', 14)

print(f"{person1.name} age: {person1.age}. Is adult: {person1.is_adult(person1.age)}")
print(f"{person2.name} age: {person2.age}. Is adult: {person2.is_adult(person2.age)}")
