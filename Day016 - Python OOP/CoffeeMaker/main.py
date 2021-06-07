from menu import Menu
from maker import CoffeeMaker
from register import Register

register = Register()
coffeeMaker = CoffeeMaker()
menu = Menu()

isOn = True

while isOn:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        isOn = False
    elif choice == "report":
        coffeeMaker.report()
        register.report()
    else:
        drink = menu.find_drink(choice)
        isEnoughIngredients = coffeeMaker.is_resource_sufficient(drink)
        isPaymentSuccessful = register.make_payment(drink.cost)
        if isEnoughIngredients and isPaymentSuccessful:
            coffeeMaker.make_coffee(drink)
