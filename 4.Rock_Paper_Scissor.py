import random
print("WELCOME TO ROCK PAPER SCISSOR GAME")
your_choice=int(input("choose 0 for ROCK,,,1 for PAPER,,, 2 for SCISSOR\n")) 
if your_choice==0:
    print("ROCK")
elif your_choice==1:
    print("PAPER")
elif your_choice==2:
    print("SCISSOR")
else:
    print("INVALID CHARACTER")
    print("Enter a number 0 or 1 0r 2")
print("COMPUTER CHOICE:")
computer_choice=random.randint(0,2)
if computer_choice==0:
    print("ROCK")
elif computer_choice==1:
    print("PAPER")
elif computer_choice==2:
    print("SCISSOR")

if computer_choice==0 and your_choice==1:
    print("YOU WIN!!!!!!")
elif computer_choice==1 and your_choice==2:
    print("YOU WIN!!!!!!")
elif computer_choice==2 and your_choice==0:
    print("YOU WIN!!!!!!")
elif computer_choice==0 and your_choice==0:
    print("BOTH CHOSE ROCK..... REGAME")
elif computer_choice==1 and your_choice==1:
    print("BOTH CHOSE PAPER..... REGAME")
elif computer_choice==2 and your_choice==2:
    print("BOTH CHOSE SCISSOR..... REGAME")
else:
    print("********COMPUTER WIN******\n YOU LOSE")