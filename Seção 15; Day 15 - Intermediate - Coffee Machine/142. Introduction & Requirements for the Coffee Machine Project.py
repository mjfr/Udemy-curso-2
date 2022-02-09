def main():
    from os import system

    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    COINS = {
        "quarters": 0.25,
        "dimes": 0.1,
        "nickles": 0.05,
        "pennies": 0.01
    }


    def calculate_resources(order):
        '''
        Parameter that gets a MENU product as an attribute\n
        Uses a loop that considers the machine resources in comparison to the product ordered\n
        Returns 0 in case of lacking ingredients\n
        Returns 1 if everything is okay
        '''
        for ingredient in MENU[order]["ingredients"]:
            if MENU[order]["ingredients"][ingredient] > resources[ingredient]+0.0001:
                print(f"Not enough {ingredient}")
                return 0
        return 1


    def use_resources(calculate_resources_result, order):
        '''
        The parameters get as attributes the return of the calculate_resources(order) function and the MENU product\n
        If it returns 1, a loop will subtract the resources used from the stored resources.
        '''
        if calculate_resources_result == 1:
            for ingredient in MENU[order]["ingredients"]:
                if MENU[order]["ingredients"].get(ingredient):
                    if (resources[ingredient] - MENU[order]["ingredients"][ingredient]) > -0.0001:
                        resources[ingredient] -= MENU[order]["ingredients"][ingredient]


    def keep_money(order):
        '''
        Just returns the value of the chosen product.
        '''
        return MENU[order]["cost"]
        

    def calculate_change(order):
        '''
        Makes a loop to ask to the user how many coins of each value will be inserted while adding the values.\n
        Returns a round value of the change the user will get.
        '''
        print("Insert coins in order:")
        value_sum = 0
        for coin in COINS:
            inserted_coins = 0
            inserted_coins += int(input(f"How many {coin}?: "))
            value_sum += (inserted_coins * COINS[coin])
        return round(MENU[order]["cost"] - value_sum, 2)*-1

    
    def enough_money(calculate_change):
        '''
        Just returns 1 or 0 depending on the calculate_change(order) function return.\n
        Returns 1 in case of the attribute value is higher than 0
        Returns 0 in case of the attribute value is lower than 0
        '''
        if calculate_change > 0.001:
            return 1
        return 0


    def coffee_machine():
        power_state = "on"
        machine_money = 0
        while power_state == "on":
            order = input("\nWhat would you like? (espresso | latte | cappuccino):\nAnswer: ").lower()
            if order == "off":
                print("Turning off the coffee machine.")
                power_state = "off"
            elif order == "report":
                system("cls")
                print(f"Water: {resources['water']}mL\nMilk: {resources['milk']}mL"
                f"\nCoffee: {resources['coffee']}g\nMoney: ${machine_money}")
            else:
                while (order != "espresso") and (order != "latte") and (order != "cappuccino"):
                    order = input(f"There is no '{order}'.\nYou can choose between espresso, latte or cappuccino."
                                f"\nAnswer: ")
                
                resources_available = calculate_resources(order)
                if resources_available == 1:
                    change = calculate_change(order)
                    if enough_money(change) == 1:
                        machine_money += keep_money(order)
                        use_resources(resources_available, order)
                        if change == 0:
                            print(f"Here is your {order} ☕. Enjoy!")
                        else:
                            print(f"Here is ${change} in change.")
                            print(f"Here is your {order} ☕. Enjoy!")
                if change < 0:
                    print("Not enough money. Your money was refunded.")


    coffee_machine()


if __name__ == "__main__":
    main()
