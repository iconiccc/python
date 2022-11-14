#Random number generator

import random

 

number_range1 = int(input("What is the first number in your range: "))
number_range2 = int(input("What is the second number in your range: "))
number_type = input("What type of number would you like to generate, you have the choices - even, odd or random: ")

number_range1 = number_range1 / 2
number_range2 = number_range2 / 2

if number_range1  %2 != 0:
    round(number_range1)
elif number_range2  %2 != 0:
    round(number_range2)


if number_type == "even":
  answer = (random.randint(int(number_range1), int(number_range2))*2)
  print(answer)       
elif number_type == "odd":
    answer = (random.randint(int(number_range1), int(number_range2))*2+1)
    print(answer)
elif number_type == "random":
    answer = (random.randint(int(number_range1), int(number_range2)))
    print(answer)



