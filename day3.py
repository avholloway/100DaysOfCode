# 3.1 - Even or odd
# ---------------------------------------------------------
def one():
  # 🚨 Don't change the code below 👇
  number = int(input("Which number do you want to check? "))
  # 🚨 Don't change the code above 👆

  #Write your code below this line 👇

  print(f"This is an {'odd' if number % 2 else 'even'} number")


# 3.2 - bmi calc 2.0
# ---------------------------------------------------------
def two():
  # 🚨 Don't change the code below 👇
  height = float(input("enter your height in m: "))
  weight = float(input("enter your weight in kg: "))
  # 🚨 Don't change the code above 👆

  #Write your code below this line 👇

  # from bmi 1.0
  bmi = round(float(weight) / (float(height) ** 2))

  print(f"Your BMI is {bmi}, ", end="")

  if bmi < 18.5:
    print("you are underweight.")
  elif bmi < 25:
    print("you have a normal weight.")
  elif bmi < 30:
    print("you are slightly overweight.")
  elif bmi < 35:
    print("you are obese.")
  else:
    print("you are clinically obese.")

# 3.3 - leap year
# ---------------------------------------------------------
def three():
  # 🚨 Don't change the code below 👇
  year = int(input("Which year do you want to check? "))
  # 🚨 Don't change the code above 👆

  #Write your code below this line 👇

  # evenly divisible by 4
  # except if also evenly divisible by 100
  # unless if also evenly divisible by 400

  # golfed example which passes 3.3 testing
  # print(f"{'Leap year.' if not (year % (4 if year % 25 else 16)) else 'Not leap year.'}")

  evenly_divisible_by_4 = not year % 4
  evenly_divisible_by_100 = not year % 100
  evenly_divisible_by_400 = not year % 400

  if evenly_divisible_by_4 and (not evenly_divisible_by_100 or evenly_divisible_by_400) :
    print("Leap year.")
  else:
    print("Not leap year.")

# 3.4 - pizza order
# ---------------------------------------------------------
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

cost = {"S": 15, "M": 20, "L": 25}[size]

if add_pepperoni == "Y":
  cost += {"S": 2, "M": 3, "L": 3}[size]

if extra_cheese == "Y":
  cost += {"S": 2, "M": 3, "L": 3}[size]

print(f"Your final bill is: {cost}.")