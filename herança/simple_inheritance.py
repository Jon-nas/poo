class vehicle:
    def __init__(self, colour, plate, number_wheels):
        self.colour = colour
        self.plate = plate
        self.number_wheels = number_wheels

    def start_engine(self):
        print("Starting the engine.")

    def __str__(self):
        return f"{self.__class__.__name__}: {", " .join([f"{key} = {value}" for key, value in self.__dict__.items()])}"

class motocycle(vehicle):
    pass

class car(vehicle):
    pass

class truck(vehicle):
    def __init__(self, colour, plate, number_wheels, load):
        super().__init__(colour, plate, number_wheels)
        self.load = load

    def load(self):
        print(f"{'Yes' if self.load else 'No'} I am loaded.")

kawasaki = motocycle("Black", "JNS-9999", 2)
mustang = car("dark blue", "JNS-9999", 4)
mercedes_benz = truck("Deep red", "JNS-9999", 46, False)

print(kawasaki)
print(mustang)
print(mercedes_benz)