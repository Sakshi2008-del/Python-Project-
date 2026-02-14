import random

number = random.randint(1, 10)
attempts = 3

while attempts > 0 :
    guess = int(input("GUESS A NUMBER (1 - 10): "))

    if guess == number :
        print("congrats you won !")
        break
    else :
        print("OOPS WRONG GUESS")
        attempts -= 1

if attempts == 0:
    print(" you lost ! number was " , number)