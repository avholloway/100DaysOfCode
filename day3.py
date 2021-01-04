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
def four():
  print("Welcome to Python Pizza Deliveries!")
  size = input("What size pizza do you want? S, M, or L ")
  add_pepperoni = input("Do you want pepperoni? Y or N ")
  extra_cheese = input("Do you want extra cheese? Y or N ")
  # 🚨 Don't change the code above 👆

  #Write your code below this line 👇

  cost = {"S": 15, "M": 20, "L": 25}.get(size, 0)
  cost += {"YS": 2, "YM": 3, "YL": 3}.get(add_pepperoni + size, 0)
  cost += {"YS": 1, "YM": 1, "YL": 1}.get(extra_cheese + size, 0)
  print(f"Your final bill is: ${cost}.")

# 3.5 - Love calc
# ---------------------------------------------------------
def five():
  # 🚨 Don't change the code below 👇
  print("Welcome to the Love Calculator!")
  name1 = input("What is your name? \n")
  name2 = input("What is their name? \n")
  # 🚨 Don't change the code above 👆

  #Write your code below this line 👇

  names = name1.lower() + name2.lower()

  true_score = 0
  for letter in "true":
    true_score += names.count(letter)

  love_score = 0
  for letter in "love":
    love_score += names.count(letter)

  score = int(f"{true_score}{love_score}")
  print(f"Your score is {score}", end="")

  if score < 10 or score > 90:
    print(", you go together like coke and mentos", end="")
  elif score > 40 and score < 50:
    print(", you are alright together", end="")

  print(".")

# Final - treasure island game
# ---------------------------------------------------------
print('''
            88                                          
            ""                         ,d               
                                       88               
8b,dPPYba,  88 8b,dPPYba, ,adPPYYba, MM88MMM ,adPPYba, ,adPPYba,  
88P'    "8a 88 88P'   "Y8 ""     `Y8   88   a8P_____88 I8[    ""  
88       d8 88 88         ,adPPPPP88   88   8PP"""""""  `"Y8ba,  
88b,   ,a8" 88 88         88,    ,88   88,  "8b,   ,aa aa    ]8I  
88`YbbdP"'  88 88         `"8bbdP"Y8   "Y888 `"Ybbd8"' `"YbbdP"'  
88                                                      
88                                                    
''')
print("\nwelcome to the game of pirates.\n")
print("where we don't use capital letters and your mission is to find the treasure.")

def play():

  # question 1
  direction = input("\nwhich way first, matey: left or right? ")
  if direction.lower() != "left":
    print("\noh no. you're not going to like this. you caught the scurves...and died. oh, yeah, what a twist.")
    return

  # question 2
  action = input("\nhigh tide in the bay, strumpet, shall we: wait or swim? ")
  if action != "wait":
    print("\nyou wench, you can't swim. say hello to davey jones for me...oh and you died.")
    return

  # question 3
  door = input("\nwhich door will it be ya bilge rat: red, blue or yellow? ")
  if door != "yellow":
    print("\naaaaaaaaaaaaaand you survived. no, actually, you died.")
    return

  print("\na left turn ye did, then waited before ye picked the yellow door. smart, smart, very smart. the treasure be yours me hearty...yo ho.")

play()