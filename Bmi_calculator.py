#BMI Calculator
import math

#taking input from user
height = float(input("enter your height in meter: "))
weight = float(input("enter your weight in kg: "))

bmi_calc = weight//pow(height, 2)

if bmi_calc < 18.5:
    print("you are underweight")
elif 18.5 < bmi_calc < 25 :
    print("you have a normal weight")
elif 25 < bmi_calc < 30:
    print("you are overweight")
elif 30 < bmi_calc < 35:
    print("obese")
else:
    print("clinically obese")
    
