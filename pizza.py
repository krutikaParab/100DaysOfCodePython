#Automated pizza order bill calculation
#takinh inputs for order
class PizzaBillCalc(self, size, add_pepperoni, extra_cheese):

    def __init__(self):
        self.size = size
        self.add_pepperoni = add_pepperoni
        self.extra_cheese = extra_cheese
    def bill_calc():
        small_pizza_price = 15
        medium_pizza_price = 20
        large_pizza_price = 25

        pepperoni_for_small = 25
        pepperoni_for_large_medum = 3

        cheese_for_any = 1

        bill = 0

        if self.size == 'Small' :
            bill += small_pizza_price
        if self.size == 'Medium':
            bill+= medium_pizza_price
        if self.size == 'Large':
            bill += large_pizza_price

        if self.add_peperoni == 'Y':
            if self.size == 'Small':
                bill += 2
            else:
                bill += 3

        if cheese_for_any == 'Y':
            bill += 1

        return bill


print("Please Customise your pizza")
size = input("what size of pizza do you want?\n1.Small\nMedium\nLarge\n")
add_pepperoni = input("Do ypu want peporani?\nYes or No\n")
extra_cheese = input("Do you want extra cheese ?\nYes or No")

p1 = PizzaBillCalc(size, add_pepperoni, extra_cheese)

p1.bill_calc()
