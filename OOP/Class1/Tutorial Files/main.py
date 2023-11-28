from item import Item
from keyboard import Keyboard
from phone import Phone


Item.instantiate_from_csv("data.csv")
print(Item.all)

phone1 = Phone("S40Lite", 200, 10, 1)
keyboard1 = Keyboard("MechV12", 75, 35)

print(keyboard1.price)
print(phone1.price)

# Inheritance and polymorphism working together
phone1.apply_discount()
keyboard1.apply_discount()

print(keyboard1.price)
print(phone1.price)



