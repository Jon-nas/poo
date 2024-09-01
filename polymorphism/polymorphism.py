class bird:
    def fly(self):
        print("Flying...")

class sparrow(bird):
    def fly(self):
        super().fly()

class ostrich(bird):
    def fly(self):
        print("Ostrich can't fly.")

def flight_plan(obj):
    obj.fly()

flight_plan(sparrow())
flight_plan(ostrich())