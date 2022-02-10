def main():
    from menu import Menu
    from coffee_maker import CoffeeMaker
    from money_machine import MoneyMachine

    menu = Menu()
    money = MoneyMachine()
    coffee_maker = CoffeeMaker()

    def repeat_coffee_input():
        user_input = input(f"What would you like? ({menu.get_items()}) ").lower()
        if user_input == "off":
            return user_input
        elif user_input == "report":
            coffee_maker.report()
            money.report()
            return "report"
        elif menu.find_drink(user_input) is None:
            return None
        return menu.find_drink(user_input)

    coffee = ""
    while coffee != "off":
        coffee = repeat_coffee_input()
        if coffee != "report" and coffee != "off" and coffee is not None:
            if coffee_maker.is_resource_sufficient(coffee):
                if money.make_payment(coffee.cost):
                    coffee_maker.make_coffee(coffee)


if __name__ == "__main__":
    main()
