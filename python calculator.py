#python calculator

import random
print("Welcome to the my calculator, here you will be able to multiply, divide and substract.")
num1 = int(input("What is your first number: "))
num2 = int(input("What is your second number: "))
operator = input("What would you like to do, multiply (*), divide (/),  substract (-) or addition (+): ")

if operator == "*":
    print("This multiplies up to: ", num1 * num2)
elif operator == "-":
    print("This substracts up to: ", num1 - num2)
elif operator == "/":
    print("This divides up to: ", num1 / num2)
elif operator == "+":
    print("This adds up to: ", num1 + num2)

