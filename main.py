from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()  

on = True

while on:
    options = my_menu.get_items()
    prompt = input(f"What would you like? ({options}) ")
    if prompt == "off":
        on = False
    elif prompt == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:  
        drink = my_menu.find_drink(prompt)
        if drink != None:
            if my_coffee_maker.is_resource_sufficient(drink):
                if my_money_machine.make_payment(drink.cost):
                    my_coffee_maker.make_coffee(drink)


        


