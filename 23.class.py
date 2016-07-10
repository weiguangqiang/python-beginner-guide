# !/usr/bin/Python

# website: http://pythonprogramminglanguage.com/class

'''
#Eg
s = [2,4,6,8]
s.reverse()
print(s)
'''

class ShoppingList:
    products = []

    # __init__ method (also called constructor) that is called when you create new object.
    def __init__(self):
        print("Shopping list created!")

    def add(self, name):
        self.products.append(name)

    def show(self):
        print(self.products)

shoplist = ShoppingList()
shoplist.add("Rice")
shoplist.add("Apple")
shoplist.show()
