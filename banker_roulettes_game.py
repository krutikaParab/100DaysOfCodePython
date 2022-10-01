#Banker Roulette Game
'''
This is the simple game where after a meal everybody puts there cards in bill book and cashier have to choose it randomly and whoseever he chooses that person have to pay bill of the meal
'''
import random

card_holders = input("Name of card holders: \n ")
card_holders_lists = card_holders.split()
pay_bill = random.choice(card_holders_lists)
print(f'{pay_bill} have to pay for todays bill....')
