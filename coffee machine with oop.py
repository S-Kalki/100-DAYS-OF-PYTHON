class CoffeeMachine:

    def __init__(self):
        self.resources = {
            "water": 1000,
            "milk": 500,
            "coffee": 200
        }

        self.money = 0

        self.menu = {
            "espresso": {
                "water": 50,
                "milk": 0,
                "coffee": 18,
                "price": 50
            },
            "latte": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
                "price": 80
            },
            "cappuccino": {
                "water": 150,
                "milk": 100,
                "coffee": 24,
                "price": 90
            }
        }

    def show_report(self):
        print("\n--- Coffee Machine Report ---")
        print("Water:", self.resources["water"], "ml")
        print("Milk:", self.resources["milk"], "ml")
        print("Coffee:", self.resources["coffee"], "g")
        print("Money: ₹", self.money)

    def check_resources(self, drink):
        required = self.menu[drink]

        if self.resources["water"] < required["water"]:
            print("Not enough water.")
            return False

        if self.resources["milk"] < required["milk"]:
            print("Not enough milk.")
            return False

        if self.resources["coffee"] < required["coffee"]:
            print("Not enough coffee.")
            return False

        return True

    def take_money(self, price):
        print("Price: ₹", price)

        money = int(input("Insert money: ₹"))

        if money < price:
            print("Not enough money. Money refunded.")
            return False

        change = money - price

        if change > 0:
            print("Change: ₹", change)

        self.money += price
        return True

    def make_coffee(self, drink):
        required = self.menu[drink]

        self.resources["water"] -= required["water"]
        self.resources["milk"] -= required["milk"]
        self.resources["coffee"] -= required["coffee"]

        print(f"Here is your {drink} ☕ Enjoy!")

    def run(self):
        while True:

            choice = input(
                "\nWhat would you like? "
                "(espresso/latte/cappuccino/report/off): "
            ).lower()

            if choice == "off":
                print("Coffee machine turned off.")
                break

            elif choice == "report":
                self.show_report()

            elif choice in self.menu:

                if self.check_resources(choice):

                    price = self.menu[choice]["price"]

                    if self.take_money(price):
                        self.make_coffee(choice)

            else:
                print("Invalid choice.")


# Create object
machine = CoffeeMachine()

# Start coffee machine
machine.run()