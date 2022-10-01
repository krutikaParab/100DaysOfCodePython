#Rock paper Scissor Game
import random

while True:
    print("Let's play Rock-Paper-Scissor with me...!")
    user_input = input("What will be your choice ????\nRock\tPaper\tScissor\n").lower()
    choice_list = ["rock","paper","scissor"]
    computer_input = random.choice(choice_list)

    if computer_input == 'rock' and user_input == 'scissor':
        print(f'Computer has selected {computer_input}.....Computer win')
    if computer_input == 'paper' and user_input == 'scissor':
        print(f'Computer has selected {computer_input}.....You Win')
    if (computer_input == 'scissor' and user_input == 'scissor') or (computer_input == 'rock' and user_input == 'rock') or (computer_input == 'paper' and user_input == 'paper'):
        print(f'Computer has selected {computer_input}.....Match Tie')
    if computer_input == 'scissor' and user_input == 'rock':
        print(f'Computer has selected {computer_input}.....You Win')
    if computer_input == 'scissor' and user_input == 'paper':
        print(f'Computer has selected {computer_input}.....Computer Win')

    game = input("Do you want to continue ??? yes or no...\n")
    if game == 'y' or game == 'yes':
        continue
    else:
        print("Thanks for playing with me")
        break
    
