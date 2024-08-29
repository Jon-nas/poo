class animal:
    def __init__(self, paws):
        self.paws = paws

    def __str__(self):
        return f"{self.__class__.__name__}: {", " .join([f"{key} = {value}" for key, value in self.__dict__.items()])}"

class mammal(animal):
    def __init__(self, colour, **kw):
        super().__init__(**kw)
        self.colour = colour

class bird(animal):
    def __init__(self, beak_colour, **kw):
        super().__init__(**kw)
        self.beak_colour = beak_colour

class cat(mammal):
    pass
    
class platypus(mammal, bird):
    def __init__(self, beak_colour, colour, paws):
        print(platypus.__mro__)
        
        super().__init__(colour = colour, beak_colour = beak_colour, paws = paws)

bills = cat(paws = 4, colour = "Black")
print(bills)

perry = platypus(paws = 4, colour = "Brown", beak_colour = "Orange")
print(perry)