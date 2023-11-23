from item import Item

class Keyboard(Item): # -> child class
    pay_rate = 0.5 # different discount
    def __init__(self, name: str, price: float, quantity: int=0):
        super().__init__(name, price, quantity)

