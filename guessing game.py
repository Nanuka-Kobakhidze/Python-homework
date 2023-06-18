#........... guessing game

import random

random_number = random.randint(0, 99)

while True:
    number = int(input("guess the correct number: "))

    if number > random_number:
        print("please guess a lower number")
    elif number < random_number:
        print("please guess a higher number")
    else:
        print("the number you guessed is correct!")
        break