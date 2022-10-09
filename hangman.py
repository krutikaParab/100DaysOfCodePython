# Building a Hangman Game
import random
# from replit import clear

# To improve UI experience
lives_list = [
    ''' 
        *--------*
        |        |
        |        O
        |       /|\\
        |        |
        |       / \\
        |
        |
    -----------
        ''',
    ''' 
            *--------*
            |        |
            |        O
            |       /|\\
            |        |
            |       /
            |
            |
        -----------
            ''',
    ''' 
            *--------*
            |        |
            |        O
            |       /|\\
            |        
            |
            |
            |
        -----------
            ''',
    ''' 
            *--------*
            |        |
            |        O
            |       /|
            |        
            |
            |
            |
        -----------
            ''',
    ''' 
            *--------*
            |        |
            |        O
            |        
            |        
            |
            |
            |
        -----------
            ''',
    ''' 
        *--------*
        |        |
        |        
        |        
        |        
        |
        |
        |
    -----------
        ''',
    ''' 
            *--------*
            |        
            |        
            |        
            |        
            |
            |
            |
        -----------
            ''',

]

lives = 6

# A word list to play game
word_list = ["ardvrk", "baboon", "camel"]

# Let's choose a random word to play game
chosen_word = random.choice(word_list)
# print(chosen_word)

# Created an empty list to display blank word if word is apple list will be ['_','_','_','_','_']
display = []
for letter in range(len(chosen_word)):
    display += "_"
print(display)

# Create a flag to stop a while loop
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        # You can use this line as a part of debugging
        # print(f"Current position: {pos}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[pos] = letter

    # lives count
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print(lives_list[0])
            end_of_game = True
            print("you lose")

    print(f"{' '.join(display)}")

    # To check end of game or not
    if "_" not in display:
        end_of_game = True
        print("You win")

    print(lives_list[lives])


