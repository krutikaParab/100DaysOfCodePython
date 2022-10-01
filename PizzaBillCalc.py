#Automated pizza order bill calculation
#takinh inputs for order
class PizzaBillCalc():

    def __init__(self, size, add_pepperoni, extra_cheese):
        self.size = size
        self.add_pepperoni = add_pepperoni
        self.extra_cheese = extra_cheese
    def bill_calc(self):
        small_pizza_price = 15
        medium_pizza_price = 20
        large_pizza_price = 25

        pepperoni_for_small = 25
        pepperoni_for_large_medium = 3

        cheese_for_any = 1

        bill = 0

        if self.size == 'Small' :
            bill += small_pizza_price
        if self.size == 'Medium':
            bill+= medium_pizza_price
        if self.size == 'Large':
            bill += large_pizza_price

        if self.add_pepperoni == 'Y':
            if self.size == 'Small':
                bill += pepperoni_for_small
            else:
                bill += pepperoni_for_large_medium

        if self.extra_cheese == 'Y':
            bill += cheese_for_any

        return bill


print("Please Customise your pizza")
size = input("what size of pizza do you want?\n1.Small\n2.Medium\n3.Large\n")
add_pepperoni = input("Do you want peporani?\nYes or No\n")
extra_cheese = input("Do you want extra cheese ?\nYes or No\n")

p1 = PizzaBillCalc(size, add_pepperoni, extra_cheese)
final_bill = p1.bill_calc()

print(f'Your pizza bill here is {final_bill}\nPlease Enjoy Your Order....!')
