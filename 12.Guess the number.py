import random

print("WELCOME TO THE NUMBER GUESSING GAME")
print("The Number is between 1 to 100")

number = random.randint(1, 100)

difficulty = input("Select the difficulty level.... EASY or HARD\n").lower()

if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    print("**********INVALID**********")
    print("Choose a level between easy or hard")
    exit()

while lives != 0:
    guess = int(input("Guess a number between 1 to 100\n"))

    lives -= 1
    print(f"You have {lives} lives left")

    if guess > number:
        print("Your guess is greater than the number. Think low.")

    elif guess < number:
        print("Your guess is lesser than the number. Think high.")

    else:
        print("You guessed the number!!!!")
        print("******* YEAH!!!! YOU WON ******")
        break

    print("<<<<>>>")

if lives == 0 and guess != number:
    print("BETTER LUCK NEXT TIME")
    print("THE NUMBER IS:", number)