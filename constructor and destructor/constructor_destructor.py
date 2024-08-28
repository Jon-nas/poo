class dog:
    def __init__(self, name, color, awake = True):
        print("Initializing the class...")
        self.name = name
        self.color = color
        self.awake = awake

    def __del__(self):
        print("removing the class instance.")

    def bark(self):
        print("wau, Wau, wau!")

def create_dog():
    dalmatian = dog("spot", "black and white", False)
    print(dalmatian.name)    

pinscher = dog("peanut", "caramel")
pinscher.bark()

print("Hello World!")

del pinscher

print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")

#create_dog()