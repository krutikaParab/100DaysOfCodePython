#Treasure Island Game
print("Welcome to Treasure Island")
print("Your mission is to findthe treasure")

choice1 = input('You\'re at crossroad, where do you want to go? Type "left" or "right"').lower()
if choice1 == "left":
    choice2 = input('You\'ve came at lake, Type "Wait" to wait for a boat or Type "Swim" to swin across').lower()
    if choice2 == 'wait':
        choice3 = input('Well Done you\'ve at Island. there is three path "Red", "Yellow", "Blue" choose carefully from these paths to win this game').lower()
        if choice3 == 'yellow':
            print("You have win this Game....Congratulations!!!!")
        else:
            Print("Your Game is over")
    else:
        Print("Your Game is over")
else:
    Print("Your Game is over")
