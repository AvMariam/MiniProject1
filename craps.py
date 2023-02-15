import random as rd

def dice_sum(a, b):
    return a + b

goal = 0
flag = 1

dice1 = rd.randint(1, 6)
dice2 = rd.randint(1, 6)

print(f"The sum of dice is {dice1} + {dice2} = {dice_sum(dice1, dice2)}")
if dice_sum(dice1, dice2) == 7 or dice_sum(dice1, dice2) == 11:
    print("Congratulations!!! You WON.")
elif dice_sum(dice1, dice2) == 2 or dice_sum(dice1, dice2) == 3 or dice_sum(dice1, dice2) == 12:
    print("I'm sorry, the casino won.")
else:
    goal = dice_sum(dice1, dice2)
    print(f"Now your goal is {goal}.")
    while flag:
        dice1 = rd.randint(1, 6)
        dice2 = rd.randint(1, 6)
        print(f"The sum of dice is {dice1} + {dice2} = {dice_sum(dice1, dice2)}")
        if dice_sum(dice1, dice2) == goal:
            print("You won.")
            flag = 0
        elif dice_sum(dice1, dice2) == 7:
            print("You lose.")
            flag = 0

