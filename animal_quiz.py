score = 0
print("Guess the animal")

def check_guess(guess, answer):
    global score   #it ensures that changes to the variable can be seen throughout the whole program
    if guess == answer:
        print("Correct Answer")
        score = score + 1
