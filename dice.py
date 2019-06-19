import random as r

def dice_roll():
    sides = 6
    rolling = True
    while rolling:
        dice_1 = r.randint(1, sides)
        dice_2 = r.randint(1, sides)
        roll_again = input("Ready to roll?/nY for Yes or N for no. ")
        if roll_again.lower() != "n":
            print(f'First dice rolled a {dice_1}')
            print(f'Second dice rolled a {dice_2}')
            print(f'Your total is {dice_1 + dice_2}')
        else:
            rolling = False

if __name__ == "__main__": dice_roll()