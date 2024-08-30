class person:
    def __init__(self, name, birthdate):
        self._name = name
        self._birthdate = birthdate

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        _present_year = 2024
        return _present_year - self._birthdate
    
personal = person("Sano", 1988)
print(f"Name: {personal.name}\tAge: {personal.age}")