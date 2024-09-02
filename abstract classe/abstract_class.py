from abc import ABC, abstractmethod

class remote(ABC):
    @abstractmethod
    def on(self):
        pass
    
    @abstractmethod
    def off(self):
        pass

    @property
    @abstractmethod
    def brand(self):
        pass

class tvControl(remote):
    def on(self):
        print("Turning on the tv...")
        print("on!")

    def off(self):
        print("Turning off the tv...")
        print("off!")

    @property
    def brand(self):
        return "Sammsam"

class conditioningAir(remote):
    def on(self):
        print("Turning on the conditioning air...")
        print("on!")

    def off(self):
        print("Turning off the conditioning air...")
        print("off!")

    @property
    def brand(self):
        return "GG"

control = tvControl()
control.on()
control.off()
print(control.brand)

control = conditioningAir()
control.on()
control.off()
print(control.brand)