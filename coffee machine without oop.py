MENU = {
    "espresso": {"water": 50, "coffee": 18, "milk": 0, "price": 50},
    "latte": {"water": 200, "coffee": 24, "milk": 150, "price": 80},
    "cappuccino": {"water": 150, "coffee": 24, "milk": 100, "price": 90}
}

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 200
}

money = 0


def check_resources(drink):
    required = MENU[drink]

    if resources["water"] < required["water"]:
        print("Sorry, not enough water.")
        return False

    if resources["milk"] < required["milk"]:
        print("Sorry, not enough milk.")
        return False

    if resources["coffee"] < required["coffee"]:
        print("Sorry, not enough coffee.")
        return False

    return True


def take_money(price):
    print(f"Price: ₹{price}")

    amount = int(input("Insert money: ₹"))

    if amount < price:
        print("Not enough money. Money refunded.")
        return False

    change = amount - price

    if change > 0:
        print(f"Here is your change: ₹{change}")

    return True


def make_coffee(drink):
    global money

    required = MENU[drink]

    resources["water"] -= required["water"]
    resources["milk"] -= required["milk"]
    resources["coffee"] -= required["coffee"]

    money += required["price"]

    print(f"Here is your {drink} ☕ Enjoy!")


def show_report():
    print("\n--- Coffee Machine Report ---")
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ₹{money}")
    print("-----------------------------")


def coffee_machine():
    while True:
        choice = input(
            "\nWhat would you like? "
            "(espresso/latte/cappuccino/report/off): "
        ).lower()

        if choice == "off":
            print("Coffee machine turned off.")
            break

        elif choice == "report":
            show_report()

        elif choice in MENU:

            if check_resources(choice):

                if take_money(MENU[choice]["price"]):
                    make_coffee(choice)

        else:
            print("Invalid choice. Please try again.")


coffee_machine()