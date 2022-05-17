###############################| Import |##################################################
from ast import Continue
from distutils.log import error
import random
from tkinter.tix import Tree
from unittest import TextTestResult
from sqlalchemy import true
from sympy import cancel
from yaml import CUnsafeLoader

###############################| Variables |##################################################
ex = True  # While True Loop Menu
dices = []  # List to save dice value
d_nums = 0  # number of dices
dice = 0  # dice art
cancel_roll = 0  # 1 cancel roll sektion after illegal input
###############################| Dictornary |##################################################

# Menu Dictornaries
menu_options = {
    1: 'D20',
    2: 'D6',
    3: 'D4',
    4: 'D8',
    5: 'D10',
    6: 'D12',
    7: 'D100',
    8: 'Exit',
}

after_roll_menu_options = {
    1: 'roll again',
    2: 'back to Selection',
    3: 'Exit',
}

###############################| Function  |##################################################

# Menu function


def menu(count, menu_options):
    for count in menu_options.keys():
        print(count, '--', menu_options[count])

# input loop
#    user_choice = input("Your choice? ")
#    text_error_mm = "Enter a number between 1 and 8!\n"
#    choice = int_input_error(user_choice, text_error_mm)


def int_input_error(input_var, error_message_text):
    while True:

        try:
            input_var = int(input_var)
            return input_var
        except ValueError:
            print(error_message_text)
            break

##############################| Menu call |##################################################


while(ex):
    menu(8, menu_options)
    user_choice = input("Your choice? (1 = default)") or 1
    text_error_mm = "Enter a number between 1 and 8!\n"
    choice = int_input_error(user_choice, text_error_mm)

    if choice == 1:
        dice = 20
    elif choice == 2:
        dice = 6
    elif choice == 3:
        dice = 4
    elif choice == 4:
        dice = 8
    elif choice == 5:
        dice = 10
    elif choice == 6:
        dice = 12
    elif choice == 7:
        dice = 100
    elif choice == 8:
        exit(0)
    else:
        print(text_error_mm)
        continue

    user_d_nums = input(f"How many D{dice} do you want to throw? (1 = default)") or 1
    text_error_nums = "Enter a integer\n"
    d_nums = int_input_error(user_d_nums, text_error_nums)

###############################| After Roll |##################################################

    while(ex):
        if cancel_roll == 0:
            for i in range(0, d_nums):
                ds = random.randint(1, dice)  # dice result for i in rang of dice number
                dices.append(ds)
                print(f"You roll {d_nums} D{dice} dice/n \n\nResult: {dices}\n\n\n")
        else:  # don't roll after illegal input (var cancel_roll == 1)
            print("Your selection must be between 1 and 3!\n")
            pass

        menu(3, after_roll_menu_options)
        user_after_roll = input("Your choice? (1 = default)") or 1
        text_error_after = "Your selection must be between 1 and 3!\n"
        after_roll = int_input_error(user_after_roll, text_error_after)
        print("\n\n")

        if after_roll == 1:
            cancel_roll = 0
            del dices[0:d_nums]
        elif after_roll == 2:
            del dices[0:d_nums]
            break
        elif after_roll == 3:
            exit(0)
        else:  # catch wrong input
            del dices[0:d_nums]
            cancel_roll = 1
