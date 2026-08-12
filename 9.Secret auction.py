print("WELCOME TO THE ANTIQUE AUCTION")

print(r"""
           (  )   (   )  )
            ) (   )  (  (
            ( )  (    ) )
            _____________
           /             \
          /   ~ ~ ~ ~ ~   \
         |   ~ ~ ~ ~ ~ ~   |
         |                 |__
         |                 |  )
         |                 | /
         |                 |/
         |                 |
         |                 |
         |                 |
         |_________________|
          \_______________/
""")

choice = "yes"
bids = {}

while choice == "yes":
    name = input("Who wants to bid? ")
    amount = int(input("How much do you want to bid? $"))

    bids[name] = amount

    choice = input("Does anyone else want to bid? (yes/no): ").lower()

max_bid = 0
winner = ""

for name, amount in bids.items():
    if amount > max_bid:
        max_bid = amount
        winner = name

print(f"\n {winner} won the auction with the highest bid of ${max_bid}.")