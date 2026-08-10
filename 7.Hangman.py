import random

hangman = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """
]

guess_words = [
    "algorithm", "volcano", "galaxy", "neuron", "enzyme", "quantum", "matrix", "polygon",
    "compiler", "firewall", "blockchain", "database", "satellite", "drone", "sensor",
    "transistor", "circuit", "hydraulic", "concrete", "polymer", "molecule", "fossil",
    "glacier", "monsoon", "hurricane", "tsunami", "reef", "ecosystem", "photosynthesis",
    "mammal", "dinosaur", "archaeology", "empire", "democracy", "constitution",
    "economics", "inflation", "portfolio", "entrepreneur", "marketing", "logistics",
    "hospital", "vaccine", "stethoscope", "nutrition", "yoga", "meditation", "guitar",
    "orchestra", "canvas", "sculpture", "cinema", "novel", "poetry", "grammar",
    "dictionary", "keyboard", "smartphone", "battery", "solar", "nuclear", "aircraft",
    "submarine", "rocket", "telescope", "microscope", "calendar", "festival", "temple",
    "passport", "backpack", "compass", "mountain", "desert", "waterfall", "forest",
    "diamond", "currency", "auction", "contract", "invoice", "warehouse", "factory",
    "tractor", "harvest", "beehive", "aquarium", "chess", "cricket", "marathon",
    "helmet", "backpropagation", "chatbot", "virtualization", "container", "linux",
    "browser", "podcast", "emoji", "recipe", "perfume", "origami", "lantern"
]

lives = 6
answer = random.choice(guess_words)

correct_letters_list = []
guessed_letters = []

placeholder = "_ " * len(answer)

print("Welcome to Hangman!\n")
print("Word:", placeholder)
print(hangman[lives])
print(f"Lives Remaining: {lives}")

game_over = False

while not game_over:

    letter = input("\nGuess a letter: ").lower()

    # Input validation
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Already guessed
    if letter in guessed_letters:
        print(f"You already guessed '{letter}'.")
        continue

    guessed_letters.append(letter)

    guess = ""

    for ch in answer:
        if ch == letter:
            guess += ch
            if ch not in correct_letters_list:
                correct_letters_list.append(ch)
        elif ch in correct_letters_list:
            guess += ch
        else:
            guess += "_"

    if letter not in answer:
        lives -= 1
        print(f"\n'{letter}' is not in the word.")

    print("\nWord :", " ".join(guess))
    print(hangman[lives])
    print(f"Lives Remaining : {lives}")
    print("Guessed Letters :", " ".join(guessed_letters))

    if "_" not in guess:
        print("\n🎉 Congratulations! You Win!")
        print("The word was:", answer)
        print(r"""
               *         *
          *         *         *
       *       *  BOOM!  *       *
          *         *         *
               *         *

            \ | /
          '-- O --'
            / | \

         CONGRATULATIONS!
          YOU WON THE GAME!
""")
        game_over = True

    elif lives == 0:
        print("\n💀 You Lose!")
        print("The word was:", answer)
        game_over = True