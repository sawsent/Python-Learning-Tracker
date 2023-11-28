import csv

class Item: # -> Parent class 

    @classmethod
    def instantiate_from_csv(cls, file):
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=str(item.get('name')),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else: 
            return False


    pay_rate = 0.8 # pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity: int=0):
        # validate received arguments
        assert price >= 0, f"Price of {name}: '{price}' is negative!"
        assert quantity >= 0, f"Quantity of {name}: '{quantity}' is negative!"

        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        # actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price
        
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value=0):
        self.__price = self.__price + self.__price * increment_value


    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        # condition: name has to be short
        if len(value) > 10:
            raise Exception(f"The name '{value}' is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"