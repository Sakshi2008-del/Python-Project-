import random
item_list = ["rock", "paper", "scissors"]

user_choice = input("enter your move = rock , paper, scissor = ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print(" both chooses same : = match tie")

elif user_choice == "rock" :
    if comp_choice == "paper" :
        print("computer wins:")
    else:
        print("congrats you win !")

elif user_choice == "paper":
    if comp_choice == "rock":
        print("congrats you win !")
    else:
        print("compurter win !")

elif user_choice == "scissor":
    if comp_choice == "rock":
        print("computer win !")
    else :
        print("congrats you win !")
