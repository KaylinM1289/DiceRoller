import random


def diceRoller():
    dice1 = 0
    dice2 = 0
    continueRolling = 'y'

    while continueRolling.lower() == 'y' or continueRolling.lower() == 'yes':
        continueRolling = input("Continue rolling? (y/n)")
        if continueRolling.lower() == 'n' or continueRolling.lower() == 'no':
            break
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'Your roll for dice 1 is: {dice1}')  # Press Ctrl+F8 to toggle the breakpoint.
        print(f'Your roll for dice 2 is: {dice2}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    diceRoller('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
