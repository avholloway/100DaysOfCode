# 5.1 - average heights
# --------------------------------------
def one():
  # 🚨 Don't change the code below 👇
  student_heights = input("Input a list of student heights ").split()
  for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
  # 🚨 Don't change the code above 👆


  #Write your code below this row 👇

  i = total_height = 0
  for student_height in student_heights:
    i += 1
    total_height += student_height
  average_height = round(total_height / i)

  print(f"Average student height is {average_height}")

# 5.2 - highest score
# --------------------------------------
def two():
  # 🚨 Don't change the code below 👇
  student_scores = input("Input a list of student scores ").split()
  for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
  print(student_scores)
  # 🚨 Don't change the code above 👆

  #Write your code below this row 👇

  high_score = 0
  for score in student_scores:
    if score > high_score:
      high_score = score
  print(f"The highest score in the class is: {high_score}")

# 5.3 - adding evens
# --------------------------------------
def three():
  #Write your code below this row 👇

  total = 0
  for i in range(1, 101):
    if i % 2 == 0:
      total += i
  print(total)

# 5.4 - fizzbuzz
# --------------------------------------
def four():
  #Write your code below this row 👇

  for i in range(1, 101):
    if i % 15 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)

# Final - Password Generator
# --------------------------------------
#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random.shuffle(letters)
pw_letters = letters[:nr_letters]

random.shuffle(numbers)
pw_numbers = numbers[:nr_numbers]

random.shuffle(symbols)
pw_symbols = symbols[:nr_symbols]

password = pw_letters + pw_numbers + pw_symbols

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print(f"Easy Level Passowrd: {''.join(password)}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(password)
print(f"Hard Level Passowrd: {''.join(password)}")