## MacApp File
## This file is used to implement code used to run scripts for Mac

import random
from ErrorReport import ErrorList
from Mac import Score

def Start():
    print("="*80)
    print()
    print("="*80)
    print(">> JoKenPô <<")
    print("="*80)
    print("[0] - Rock")
    print("[1] - Paper")
    print("[2] - Scissors")
    print("="*80)
    P1 = int(input(">> Choose an option to play: "))
    CPU = random.randint(0,2)
    print("="*80)

    if P1 == 0:
        print(">> You chose: Rock")
        if CPU == 0:
            print(">> CPU chose: Rock")
            print(">> Draw: The game is tied!")
            Score.Game_Draws += 1
        elif CPU == 1:
            print(">> CPU chose: Paper")
            print(">> CPU wins!")
            Score.CPU_Wins += 1
        elif CPU == 2:
            print(">> CPU chose: Scissors")
            print(">> You win!")
            Score.P1_Wins += 1
        else:
            print(">> Invalid option")

    if P1 == 1:
        print(">> You chose: Paper")
        if CPU == 0:
            print(">> CPU chose: Rock")
            print(">> You win!")
            Score.P1_Wins += 1
        elif CPU == 1:
            print(">> CPU chose: Paper")
            print(">> Draw: The game is tied!")
            Score.Game_Draws += 1
        elif CPU == 2:
            print(">> CPU chose: Scissors")
            print(">> CPU win!")
            Score.CPU_Wins += 1
        else:
            print(">> Invalid option")
            
    if P1 == 2:
        print(">> You chose: Scissors")
        if CPU == 0:
            print(">> CPU chose: Rock")
            print(">> CPU win!")
            Score.CPU_Wins += 1
        elif CPU == 1:
            print(">> CPU chose: Paper")
            print(">> Você win!")
            Score.P1_Wins += 1
        elif CPU == 2:
            print(">> CPU chose: Scissors")
            print(">> Draw: The game is tied!")
            Score.Game_Draws += 1
        else:
            print(">> Invalid option")
    print("="*80)

def Results():
    print("="*80)
    print(">> Results <<")
    print("="*80)
    print(f'>> Wins [P1]: {Score.P1_Wins} Win(s)')
    print(f'>> Wins [CPU]: {Score.CPU_Wins} Win(s)')
    print(f'>> Total Draws: {Score.Game_Draws} Draw(s)')
    print("="*80)

def Main():
    Loop = True
    while Loop == True:
        print()
        print("="*80)
        print(">> Menu <<")
        print("="*80)
        print(">>[1] - Start Game")
        print(">>[2] - Results")
        print("="*80)

        Opc = int(input(">> Type the option number: "))

        if Opc == 1:
            Start()
        else:
            Loop = False
            Results()
         
Main()