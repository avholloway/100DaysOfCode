# 2.1 - Take a 2-digit input and add them together
# ================================================
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

number1, number2 = [int(number) for number in two_digit_number]
print(f"{number1} + {number2} = {number1 + number2}")

# 2.2 - BMI Calc
# ================================================
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(float(weight) / (float(height) ** 2), 2)
print(f"{bmi=}")

# 2.3 - Life in weeks
# ================================================
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)

years_in_life = 90

days_in_year = 365
weeks_in_year = 52
months_in_year = 12

years_remaining = years_in_life - age
months_remaining = years_remaining * months_in_year
weeks_remaining = years_remaining * weeks_in_year
days_remaining = years_remaining * days_in_year

print(f"{years_remaining=}")
print(f"{months_remaining=}")
print(f"{weeks_remaining=}")
print(f"{days_remaining=}")

# Final - Bill and Tip Calculator
# ================================================

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calc")
subtotal = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you liket to give? "))
people = int(input("How many people to split the bill? "))

total = round(subtotal * ((tip / 100) + 1), 2)
individual = round(total / people, 2)

print(f"A {tip}% tip on ${subtotal} split {people} ways, yields ${individual}")