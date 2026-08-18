import random

print(r"""
██╗  ██╗██╗ ██████╗ ██╗  ██╗███████╗██████╗      ██╗      ██████╗ ██╗    ██╗███████╗██████╗
██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗     ██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗
███████║██║██║  ███╗███████║█████╗  ██████╔╝     ██║     ██║   ██║██║ █╗ ██║█████╗  ██████╔╝
██╔══██║██║██║   ██║██╔══██║██╔══╝  ██╔══██╗     ██║     ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
██║  ██║██║╚██████╔╝██║  ██║███████╗██║  ██║     ███████╗╚██████╔╝╚███╔███╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
""")

indian_celebrities = {
    "Rajinikanth": ["Tamil", 170, "Actor, Producer, Screenwriter"],
    "Kamal Haasan": ["Tamil", 230, "Actor, Director, Producer, Singer"],
    "Vijay": ["Tamil", 68, "Actor, Singer"],
    "Ajith Kumar": ["Tamil", 62, "Actor, Racer"],
    "Suriya": ["Tamil", 45, "Actor, Producer"],
    "Vikram": ["Tamil", 60, "Actor, Singer"],
    "Dhanush": ["Tamil", 55, "Actor, Producer, Singer, Lyricist"],
    "Sivakarthikeyan": ["Tamil", 25, "Actor, Singer, TV Host"],
    "Karthi": ["Tamil", 30, "Actor"],
    "Jayam Ravi": ["Tamil", 33, "Actor"],
    "Mammootty": ["Malayalam", 420, "Actor, Producer"],
    "Mohanlal": ["Malayalam", 360, "Actor, Producer, Singer"],
    "Dulquer Salmaan": ["Malayalam", 40, "Actor, Producer"],
    "Prithviraj Sukumaran": ["Malayalam", 120, "Actor, Director, Producer"],
    "Fahadh Faasil": ["Malayalam", 55, "Actor, Producer"],
    "Chiranjeevi": ["Telugu", 155, "Actor, Producer"],
    "Pawan Kalyan": ["Telugu", 30, "Actor, Politician"],
    "Mahesh Babu": ["Telugu", 30, "Actor, Producer"],
    "Prabhas": ["Telugu", 25, "Actor"],
    "Allu Arjun": ["Telugu", 25, "Actor, Dancer"],
    "Jr NTR": ["Telugu", 32, "Actor, Singer"],
    "Ram Charan": ["Telugu", 17, "Actor, Producer"],
    "Nani": ["Telugu", 38, "Actor, Producer"],
    "Ravi Teja": ["Telugu", 75, "Actor"],
    "Nagarjuna": ["Telugu", 100, "Actor, Producer"],
    "Amitabh Bachchan": ["Hindi", 210, "Actor, Producer, TV Host"],
    "Shah Rukh Khan": ["Hindi", 95, "Actor, Producer"],
    "Salman Khan": ["Hindi", 110, "Actor, Producer, Singer"],
    "Aamir Khan": ["Hindi", 45, "Actor, Producer, Director"],
    "Akshay Kumar": ["Hindi", 150, "Actor, Producer"],
    "Hrithik Roshan": ["Hindi", 30, "Actor, Dancer"],
    "Ranbir Kapoor": ["Hindi", 22, "Actor"],
    "Ranveer Singh": ["Hindi", 20, "Actor"],
    "Ajay Devgn": ["Hindi", 130, "Actor, Director, Producer"],
    "John Abraham": ["Hindi", 50, "Actor, Producer"],
    "Deepika Padukone": ["Hindi", 38, "Actress, Producer"],
    "Alia Bhatt": ["Hindi", 25, "Actress, Producer, Singer"],
    "Kareena Kapoor": ["Hindi", 70, "Actress"],
    "Katrina Kaif": ["Hindi", 45, "Actress"],
    "Anushka Sharma": ["Hindi", 20, "Actress, Producer"],
    "Nayanthara": ["Tamil", 85, "Actress, Producer"],
    "Trisha": ["Tamil", 75, "Actress"],
    "Samantha Ruth Prabhu": ["Telugu/Tamil", 65, "Actress"],
    "Keerthy Suresh": ["Tamil/Telugu", 40, "Actress"],
    "Sai Pallavi": ["Tamil/Telugu/Malayalam", 22, "Actress, Dancer"],
    "Rashmika Mandanna": ["Kannada/Telugu/Hindi", 25, "Actress"],
    "Pooja Hegde": ["Telugu/Hindi", 22, "Actress"],
    "Yash": ["Kannada", 20, "Actor"],
    "Sudeep": ["Kannada", 60, "Actor, Director, Singer"],
    "Puneeth Rajkumar": ["Kannada", 45, "Actor, Singer, Producer"],
    "Rishab Shetty": ["Kannada", 18, "Actor, Director, Writer"],
    "Rakshit Shetty": ["Kannada", 15, "Actor, Director, Producer"],
    "Madhavan": ["Tamil/Hindi", 55, "Actor, Director, Producer"],
    "Aishwarya Rai": ["Hindi/Tamil", 50, "Actress, Model"],
    "Kajal Aggarwal": ["Tamil/Telugu", 60, "Actress"]
}

points = 0
game_on = True

while game_on:

    celebrity_A = random.choice(list(indian_celebrities.keys()))
    celebrity_B = random.choice(list(indian_celebrities.keys()))

    while celebrity_A == celebrity_B:
        celebrity_B = random.choice(list(indian_celebrities.keys()))

    print("\n---------------------------------------")

    print("Celebrity A")
    print("Name     :", celebrity_A)
    print("Industry :", indian_celebrities[celebrity_A][0])
    print("Talent   :", indian_celebrities[celebrity_A][2])

    print("\nVS\n")

    print("Celebrity B")
    print("Name     :", celebrity_B)
    print("Industry :", indian_celebrities[celebrity_B][0])
    print("Talent   :", indian_celebrities[celebrity_B][2])

    choice = input("\nWho has acted in more movies? (A/B): ").upper()

    movies_A = indian_celebrities[celebrity_A][1]
    movies_B = indian_celebrities[celebrity_B][1]

    if movies_A > movies_B:
        correct = "A"
    elif movies_B > movies_A:
        correct = "B"
    else:
        correct = "TIE"

    if correct == "TIE":
        print("\nBoth have acted in the same number of movies!")
        print("You get 1 point.")
        points += 1

    elif choice == correct:
        print("\nCorrect!")
        points += 1

    else:
        print("\nWrong!")
        print(f"{celebrity_A}: {movies_A} movies")
        print(f"{celebrity_B}: {movies_B} movies")
        print("Game Over!")
        print("Final Score:", points)
        game_on = False

    if game_on:
        print("Current Score:", points)