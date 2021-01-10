# 10.1
# ---------------------------------------------------
def one():
    def is_leap(year):
        if year % 4 == 0:
            if year % 100 == 0:
                return year % 400 == 0
            else:
                return True
        else:
            return False

    def days_in_month(year, month):
        """Take a year and month number, and return the numbers of days"""
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = month_days[month - 1]
        if month == 2 and is_leap(year):
            days += 1
        return days
    
    
    #🚨 Do NOT change any of the code below 
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)
    print(days)

# Final
# ---------------------------------------------------
from calcart import logo
print(logo)

def add(n1, n2):
    """Return the sum of two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Return the difference of two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Return the product of two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Return the quotient of two numbers."""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# get the first number in the operation
num1 = float(input("n1: "))

# get all of the other numbers in all future operations
while True:

    # get the operator for this operation
    op = input(f"operation ({', '.join(operations.keys())}): ")

    # get the number for this operation
    num2 = float(input("n2: "))

    # calculate the operation and receive the answer
    ans = operations[op](num1, num2)

    # print the solved equation to the screen
    print(f"{num1} {op} {num2} = {ans}")

    # set the answer of this operation as the first number for our next operation
    num1 = ans
    
    # though, we do need to ask if there will be a next operation
    choice = input("keep calculating (yes/no/new): ")

    if choice == "yes":
        continue

if choice == "new":
    num1 = int(input("n1: "))
    continue
    
    # if choice == "no" or really anything else, we're done here
    break
    