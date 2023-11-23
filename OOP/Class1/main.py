from item import Item


item1 = Item("MyItem", 500, 5)

item1.__name = "changed"
print(item1.__name)
item1.name()
print(item1.name)