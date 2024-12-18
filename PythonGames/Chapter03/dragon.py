import time
import random

def displayIntro():
    print('''You are in a land full of dragons, In front of you, you see two caves. In one cave, the dragon is friendly
        and will share his treasures to you, the other dragon is greedy and hungry, and will eat you on sight ''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('which cave you want to choose? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('you approach the cave')
    time.sleep(2)
    print('It\'s dark and spooky')
    time.sleep(2)
    print("a large dragon jumps out in front of you, he opens his jaws and ....")
    time.sleep(2)

    friendlyCave = random.randint(1,2)
    if(chosenCave == str(friendlyCave)):
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print("Do you want to play again? (yes or no)")
    playAgain = input()