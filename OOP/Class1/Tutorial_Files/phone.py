from item import Item

class Phone(Item): # -> child class

    def __init__(self, name: str, price: float, quantity: int=0, broken_phones: int=0):
        super().__init__(name, price, quantity)

        # validate received arguments
        assert broken_phones >= 0, f"Broken phones of {name}: '{broken_phones}' is negative!"
        self.broken_phones = broken_phones