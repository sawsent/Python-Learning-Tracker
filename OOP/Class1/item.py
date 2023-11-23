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
        self.price = price
        self.quantity = quantity
        
        # actions to execute
        Item.all.append(self)
        
    @property
    def name(self):
        return self.__name

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"