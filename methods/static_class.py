class person:
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age

    @classmethod
    def birthdate(cls, year, month, day, name):
        age = 2024 - year
        return cls(name, age)

    @staticmethod
    def older_age(age):
        return age >= 18
#p = person("Raj", 28)
#print(p.name, p.age)

p2 = person.birthdate(1994, 8, 12, "Raj")
print(p2.name, p2.age)

print(person.older_age(17))
print(person.older_age(28))