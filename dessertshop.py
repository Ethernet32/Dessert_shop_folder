from dessert import (
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)
from receipt import *

class DessertShop():
    def user_prompt_cookie(self):
        type = input("Enter the type of cookie: ")
        quantity = input("Enter the quantity purchased: ")
        price = input("Enter the price per dozen: ")
        return Cookie(type,int(quantity),float(price))
    def user_prompt_candy(self):
        type = input("Enter the type of candy: ")
        quantity = input("Enter the amount in pounds purchased: ")
        price = input("Enter the price per pound: ")
        return Candy(type,int(quantity),float(price))
    def user_prompt_icecream(self):
        type = input("Enter the type of ice cream: ")
        quantity = input("Enter the number of scoops: ")
        price = input("Enter the price per scoop: ")
        return Candy(type,int(quantity),float(price))
    def user_prompt_sundae(self):
        type = input("Enter the type of ice cream: ")
        quantity = input("Enter the number of scoops: ")
        price = input("Enter the price per scoop: ")
        topping = input("Enter the topping: ")
        tprice = input("Enter the price for the topping: ")
        return Candy(type,int(quantity),float(price), topping, float(tprice))

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
    shop = DessertShop()
    order = Order()
    '''
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    '''
    # boolean done = false
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
            '1: Candy',
            '2: Cookie',
            '3: Ice Cream',
            '4: Sunday',
            '\nWhat would you like to add to the order? (1-4, Enter for done): '
        ])
    while not done:
        choice = input(prompt)
        match choice:
            case '':
                done = True
            case '1':
                item = shop.user_prompt_candy()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '2':
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '3':
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '4':
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case _:
                print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
    print()
    DATA = [ 
        [ "Name" , "Price", "Tax"]
    ]
    for item in order.order:
        DATA.append([item.name,"$"+str(round(item.calculate_cost(),2)), "$"+str(round(item.calculate_tax(),2)) ])
    DATA.append(["Subtotal", "$"+str(round(order.order_cost(),2)), "$"+str(round(order.order_tax(),2))])
    DATA.append(["Total", "", "$"+str(round(order.order_cost()+order.order_tax(),2))]) 
    DATA.append(["Total items in the order","", len(order), ])
    make_receipt(DATA,"reciept.pdf")
main()
