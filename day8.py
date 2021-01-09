# 8.1
# -----------------------------------------------
def one():
    # Review: 
    # Create a function called greet(). 
    # Write 3 print statements inside the function.
    # Call the greet() function and run your code.

    def greet():
        print("a")
        print("b")
        print("c")

    greet()

    def greet_name(name):
        print(f"hello {name}")

    greet_name("anthony")

    def greet_with(name, location):
        greet_name(name)
        print(f"what's is like in {location}")

    greet_with("anthony", "minneapolis")

# 8.2
# -----------------------------------------------
def two():
    #Write your code below this line 👇
    from math import ceil
    def paint_calc(height, width, cover):
        print(f"You'll need {ceil(height * width / cover)} cans of paint.")

    #Write your code above this line 👆
    # Define a function called paint_calc() so that the code below works.   

    # 🚨 Don't change the code below 👇
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    paint_calc(height=test_h, width=test_w, cover=coverage)

# 8.3
# -----------------------------------------------
def three():
    import math
    def prime_checker(number):
        for i in range(2, math.isqrt(number) + 1):
            if number % i == 0:
                print("It's not a prime number.")
                return
        print("It's a prime number.")

# final
# -----------------------------------------------
from caesarart import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):

    # keep the integrity of the shift amount
    shift = shift % len(alphabet)

    # perform the shift on the readable alphabet
    shifted = alphabet[shift:] + alphabet[:shift]
    
    # set the direction of our encoding/decoding
    if direction == "encode":
        input_family = alphabet
        output_family = shifted
    else:
        input_family = shifted
        output_family = alphabet

    # initalize our results container
    result = ""

    # loop over each letter in the input text
    for letter in text:

        # only perform the transform on letters we are able to
        # and for all others, just keep them the same. e.g., spaces
        if letter in input_family:
            result += output_family[input_family.index(letter)]
        else:
            result += letter
        
    # print our result
    print(result)

def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

print(logo)
print()

main()
while input("again? ") == "yes":
    main()
print("bye")