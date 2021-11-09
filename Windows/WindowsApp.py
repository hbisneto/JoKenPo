## WindowsApp File
## This file is used to implement code used to run scripts for Windows

from ErrorReport import ErrorList
from Windows import Score
import random

def Start():
    print("="*80)
    print()
    print("="*80)
    print(">> JoKenPô <<")
    print("="*80)
    print("[0] - Pedra")
    print("[1] - Papel")
    print("[2] - Tesoura")
    print("="*80)
    P1 = int(input(">> Escolha uma opção para jogar: "))
    CPU = random.randint(0,2)
    print("="*80)

    if P1 == 0:
        print(">> Você escolheu: Pedra")
        if CPU == 0:
            print(">> CPU escolheu: Pedra")
            print(">> Empate: Não há ganhadores!")
            Score.Game_Draws += 1
        elif CPU == 1:
            print(">> CPU escolheu: Papel")
            print(">> CPU venceu!")
            Score.CPU_Wins += 1
        elif CPU == 2:
            print(">> CPU escolheu: Tesoura")
            print(">> Você venceu!")
            Score.P1_Wins += 1
        else:
            print("Opção inválida")

    if P1 == 1:
        print(">> Você escolheu: Papel")
        if CPU == 0:
            print(">> CPU escolheu: Pedra")
            print(">> Você venceu!")
            Score.P1_Wins += 1
        elif CPU == 1:
            print(">> CPU escolheu: Papel")
            print(">> Empate: Não há ganhadores!")
            Score.Game_Draws += 1
        elif CPU == 2:
            print(">> CPU escolheu: Tesoura")
            print(">> CPU venceu!")
            Score.CPU_Wins += 1
        else:
            print("Opção inválida")
            
    if P1 == 2:
        print(">> Você escolheu: Tesoura")
        if CPU == 0:
            print(">> CPU escolheu: Pedra")
            print(">> CPU venceu!")
            Score.CPU_Wins += 1
        elif CPU == 1:
            print(">> CPU escolheu: Papel")
            print(">> Você venceu!")
            Score.P1_Wins += 1
        elif CPU == 2:
            print(">> CPU escolheu: Tesoura")
            print(">> Empate: Não há ganhadores!")
            Score.Game_Draws += 1
        else:
            print("Opção inválida")
    print("="*80)

def Results():
    print("="*80)
    print(">> Resultados <<")
    print("="*80)
    print(f'>> Vitórias [P1]: {Score.P1_Wins} vitória(s)')
    print(f'>> Vitórias [CPU]: {Score.CPU_Wins} vitória(s)')
    print(f'>> Total de Empates: {Score.Game_Draws} empate(s)')
    print("="*80)

def Main():
    Loop = True
    while Loop == True:
        print()
        print("="*80)
        print(">> Menu <<")
        print("="*80)
        print(">>[1] - Iniciar Jogo")
        print(">>[2] - Resultados")
        print("="*80)

        Opc = int(input(">> Insira o número da opção desejada: "))

        if Opc == 1:
            Start()
        else:
            Loop = False
            Results()
         
Main()
