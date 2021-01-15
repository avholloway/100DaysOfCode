from instagramdata import data
from random import shuffle
from replit import clear

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

score = 0
while True:
    clear()
    print(logo)
    print()
    
    # keep the user updated on their score, if they have one
    if score > 0:
        print(f"You're right! Current score: {score}.")
        print()

    # pick our two people
    shuffle(data)
    instas = data[:2]

    # let them know who A is
    print(f"Compare A: {instas[0]['name']}, a {instas[0]['description']}, from {instas[0]['country']}.")

    # print fancy VS mini logo
    print(vs)

    # let them know who B is
    print(f"Against B: {instas[1]['name']}, a {instas[1]['description']}, from {instas[1]['country']}.")

    # determine for ourselves who the winner is
    winner = "A" if instas[0]['follower_count'] > instas[1]['follower_count'] else "B"

    # ask the user who they think the winner is
    print()
    guess = input("Who has more followers? Type 'A' or 'B': ")

    # if they were wrong, just quit
    if guess != winner:
        break

    # else, increment the score and keep it going...
    score += 1

clear()
print(logo)
print()
print(f"Sorry, that's wrong. Final score: {score}")