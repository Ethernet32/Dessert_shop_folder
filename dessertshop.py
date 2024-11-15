from dessert import (
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)
from receipt import *

class Order():
    def __init__(self):
        self.order=[]

    def add(self,other):
        self.order.append(other)

    def order_cost(self):
        total = 0.0
        for dessert in self.order:
            total+= dessert.calculate_cost()
        return round(total,2)
    
    def order_tax(self):
        total = 0.0
        for dessert in self.order:
            total+= dessert.calculate_tax()
        return round(total,2)


def main():
    order1 = Order()
    order1.add(Candy("Candy Corn", 1.5, .25))
    order1.add(Candy("Gummy Bears", .25, .35))
    order1.add( Cookie("Chocolate Chip", 6, 3.99))
    order1.add(IceCream("Pistachio", 2, .79))
    order1.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order1.add(Cookie("Oatmeal Raisin", 2, 3.45))
    total_item = 0
    for item in order1.order:
        print(item)
        total_item += 1
    print(f"Total number of items in order: {total_item}")
    DATA = [ 
        [ "Name" , "Price", "Tax"]
    ]
    for item in order1.order:
        DATA.append([item.name,"$"+str(round(item.calculate_cost(),2)), "$"+str(round(item.calculate_tax(),2)) ])
    DATA.append(["Subtotal", "$"+str(round(order1.order_cost(),2)), "$"+str(round(order1.order_tax(),2))])
    DATA.append(["Total", "", "$"+str(round(order1.order_cost()+order1.order_tax(),2))]) 
    DATA.append(["Total items in the order","", str(total_item), ])
    make_receipt(DATA,"reciept.pdf")
main()
