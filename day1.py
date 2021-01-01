# 1.1
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# 1.2
print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# 1.3
name = input("name: ")
print(f"{len(name)=}")

# 1.4
a = input("a: ")
b = input("b: ")
a, b = b, a
print(f"{a=}\n{b=}")

# Final - Band Name Generator

#1. Create a greeting for your program.
print("Anthony's Band Name Generator!")
print("=" * 80)
print()

#2. Ask the user for the city that they grew up in.
city_name = input("What city are you from?\n")

#3. Ask the user for the name of a pet.
pet_name = input("What pet name do you like most?\n")

#4. Combine the name of their city and pet and show them their band name.
band_name = f"{city_name} {pet_name}"
print(f"Your band name should be '{band_name}'")

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/