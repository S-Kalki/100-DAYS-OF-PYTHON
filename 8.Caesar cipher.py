logo = """
   _____                            _____ _       _               
  / ____|                          / ____(_)     | |              
 | |     __ _  ___  ___  __ _ _ __| |     _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__| |    | | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |  | |____| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|   \_____|_| .__/|_| |_|\___|_|   
                                           | |                    
                                           |_|                    
"""

print(logo)

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(choose, original, shift):
    output = ""


    if choose == "decrypt":
        shift *= -1

    for char in original:
        if char not in letters:
            output += char
        else:
            word_index = letters.index(char)
            new_index = (word_index + shift) % 26
            output += letters[new_index]

    print(f"\nThe {choose}ed text is: {output}\n")


game_over = False

while not game_over:
    choose = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt:\n").lower()

    if choose not in ["encrypt", "decrypt"]:
        print("Invalid choice! Please enter 'encrypt' or 'decrypt'.\n")
        continue

    original = input("Enter your message:\n").lower()

    shift = int(input("Enter shift number:\n"))
    shift %= 26

    caesar(choose, original, shift)

    choice = input("Do you want to continue? Type 'yes' or 'no': ").lower()

    if choice == "no":
        print("\nGoodbye! ")
        game_over = True