class bike:
    def __init__(self, color, model, hoop, year, value):
        self.color = color
        self.model = model
        self.hoop = hoop
        self.year = year
        self.value = value

    def horn(self):
        print("Trimmmm!")

    def stop(self):
        print("Thsssssss...")
        print("Bike Stopped.")   

    def run(self):
        print("Zummm!")

    #def __str__(self):
    #    return f"bike: color={self.color}, model={self.model}, year={self.year}, value={self.value}"

    def __str__(self):
        return f"{self.__class__.__name__}: {", " .join([f"{key} = {value}" for key, value in self.__dict__.items()])}"

#caloi = bike("red", "Vulcan", 2024, 1000)
#caloi.horn()
#caloi.stop()
#caloi.run()
#print(caloi.color, caloi.model, caloi.year, caloi.value)

monark = bike("Green", "Circular Bar", 27, 1987, 800)
print(monark)