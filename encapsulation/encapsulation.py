class account:
    def __init__(self, agency_number, balance = 0):
        self.agency_number = agency_number
        self._balance = balance

    def deposit(self, price):
        #...
        self._balance += price

    def draw(self, price):
        #...
        self._balance -= price

    def show_balance(self):
        #...
        return self._balance

count = account("001", 100)
count.deposit(100)
print(count.agency_number)
print(count.show_balance())