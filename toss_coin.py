#Tossing a coin using a random module
import random
coin_sides = ["Head", "Tail"]
print("Tossing a coin")
random_toss = random.choice(coin_sides)
print(f'{random_toss}')
