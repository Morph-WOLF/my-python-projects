import random as r

user_wins = 0
USER_WINS = user_wins
pc_wins = 0
try:
    max_runs = int(input("How many times you wanna lose"))
except ValueError:
    print("ENTER A FREAKING INTEAGER ONLY dont try to break this.")
current_runs = 1
"""Logic to compare inputs"""
rock = "r"
paper = "p"
sissor= "s"
rock > sissor
paper > rock
sissor > paper
Allowed_to_pick = [rock, paper, sissor]

"""Main shit happens here (BOI.) """
while max_runs >= current_runs:
    current_runs += 1
    print(f"Round {current_runs - 1} fight !")
    user_input = input('Rock, Paper or sissors')
    user_input.lower()
    PC_input = r.choice(Allowed_to_pick)
    print(PC_input)
    if user_input == rock and PC_input == sissor:
        user_wins += 1
        print(f"User {user_wins}\nPC {pc_wins}")
    elif user_input == paper and PC_input == rock:
        user_wins += 1
        print(f"User {user_wins}\nPC {pc_wins}")
    elif user_input == sissor and PC_input == paper:
        user_wins += 1
        print(f"User {user_wins}\nPC {pc_wins}")
    elif PC_input == rock and user_input == sissor:
        pc_wins += 1
        print(f"User {user_wins}\nPC {pc_wins}")
    elif PC_input == paper and user_input == rock :
        pc_wins += 1
        print(f"User {user_wins}\nPC {pc_wins}")
    elif PC_input == sissor and user_input == paper:
        pc_wins += 1
        print(f"User {user_wins}\nPC {pc_wins}")
    elif PC_input == user_input:
        print("TIE.")
    else:
        current_runs += -1
        print("You have entered an incorrect value")
if pc_wins > user_wins:
    print("Happy ? \nYou lost")
elif user_wins > pc_wins:
    print("consider yourself lucky kid. \nyou won")
elif pc_wins == user_wins:
    print("You lucked out. \nwe Tied.")