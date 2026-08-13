import random

# -------------------- CARDS -------------------- #

cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}


# -------------------- FUNCTIONS -------------------- #

def create_deck():
    deck = []

    for _ in range(4):  # Four suits
        for card in cards:
            deck.append(card)

    random.shuffle(deck)
    return deck


def deal_card(deck):
    if len(deck) == 0:
        print("\nDeck is empty! Reshuffling...\n")
        deck.extend(create_deck())

    return deck.pop()


def calculate_score(hand):
    score = 0
    aces = 0

    for card in hand:
        score += cards[card]
        if card == "A":
            aces += 1

    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score


def display_player(player):
    print(f"\nYour cards: {player}")
    print(f"Your score: {calculate_score(player)}")


def display_dealer_hidden(dealer):
    print(f"Dealer cards: [{dealer[0]}, ?]")


def display_dealer(dealer):
    print(f"\nDealer cards: {dealer}")
    print(f"Dealer score: {calculate_score(dealer)}")


def check_blackjack(hand):
    return len(hand) == 2 and calculate_score(hand) == 21


# -------------------- GAME -------------------- #

def play_game():

    deck = create_deck()

    player = []
    dealer = []

    player.append(deal_card(deck))
    dealer.append(deal_card(deck))
    player.append(deal_card(deck))
    dealer.append(deal_card(deck))

    print("\n========== BLACKJACK ==========")

    display_player(player)
    display_dealer_hidden(dealer)

    player_blackjack = check_blackjack(player)
    dealer_blackjack = check_blackjack(dealer)

    # ---------- Natural Blackjack ---------- #

    if player_blackjack and dealer_blackjack:
        display_dealer(dealer)
        print("\nBoth have Blackjack!")
        print("PUSH (Tie)")
        return

    elif player_blackjack:
        display_dealer(dealer)
        print("\nBLACKJACK!!")
        print("YOU WIN!")
        return

    elif dealer_blackjack:
        display_dealer(dealer)
        print("\nDealer has Blackjack!")
        print("YOU LOSE!")
        return

    # ---------- Player Turn ---------- #

    while True:

        choice = input("\nHit or Stand? (h/s): ").lower()

        if choice not in ["h", "s"]:
            print("Invalid choice.")
            continue

        if choice == "s":
            break

        player.append(deal_card(deck))

        display_player(player)
        display_dealer_hidden(dealer)

        if calculate_score(player) > 21:
            print("\nBUST!")
            print("Dealer Wins!")
            return

    # ---------- Dealer Turn ---------- #

    print("\nDealer's Turn")

    display_dealer(dealer)

    while calculate_score(dealer) < 17:

        print("Dealer Hits...")

        dealer.append(deal_card(deck))

        display_dealer(dealer)

        if calculate_score(dealer) > 21:
            print("\nDealer Busts!")
            print("YOU WIN!")
            return

    # ---------- Compare Scores ---------- #

    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)

    print("\n========== RESULT ==========")

    display_player(player)
    display_dealer(dealer)

    if player_score > dealer_score:
        print("\nYOU WIN!")

    elif dealer_score > player_score:
        print("\nDealer Wins!")

    else:
        print("\nPUSH (Tie)")


# -------------------- MAIN LOOP -------------------- #

print("WELCOME TO BLACKJACK")

while True:

    play_game()

    again = input("\nPlay Again? (y/n): ").lower()

    while again not in ["y", "n"]:
        again = input("Enter y or n: ").lower()

    if again == "n":
        print("\nThanks for playing!")
        break