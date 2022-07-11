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
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """retuened true when ingredients are enough, false when not"""
    for item in order_ingredients:
        if  order_ingredients[item] >= resources[item] :
            print(f"Sorry there is not enough {item}.")
            return False
    return True




def process_coins():
    """returnes the total calculated coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters? :")) * 0.25
    total += int(input("How many dimes? :")) * 0.1
    total += int(input("How many nickles? :")) * 0.05
    total += int(input("How many pennies? :")) * 0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    """Return True if enough money, False if not sufficient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"here's your ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money, get your refund")
        return False


is_on = True

while is_on:
    userInput = input("What would you like? (espresso\latte\cappuccino)")
    if userInput == "off":
        is_on = False

    elif userInput == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${str(profit)}")

    else:
        drink = MENU[userInput]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])