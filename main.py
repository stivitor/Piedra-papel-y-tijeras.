from data import data, menu
import random as rd
import time
import os


def clearConsole():
    
    return os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def settings(name, userPoints, machinePoints):
    
    
    userWins = ("{} : {}" .format(name, userPoints))
    machineWins = ("{} : {}" .format("Machine", machinePoints))
    print(data[2])
    print("            " + userWins)
    print("            " + machineWins)
    print(data[3])


def playGame():
    
    optionsForMachine = list(menu.values())
    print(data[0])
    nReplay = int(input("Elija el numero de jugadas: "))
    name = input("introduzca su nombre: ")
    clearConsole()
    userPoints =  + 0
    machinePoints = + 0
    settings(name, userPoints, machinePoints)
    attemps = 0

    while attemps < nReplay:
        
        clearConsole()
        
        settings(name, userPoints, machinePoints) 
        print("\n1: {} \n2: {} \n3: {} \n-" .format(menu[1], menu[2], menu[3]))
        machineOption = rd.choice(optionsForMachine)
        indexOfMachineOption = machineOption.index(machineOption)
        user = int(input("Que elijes: "))

        if user - 1 == indexOfMachineOption:
            print("Parece que es un empate XD")
            attemps -= 1
            time.sleep(2)

        elif user == 1 and machineOption == "papel":
            print("La maquina elige: " + machineOption)
            print("Has perdido :( ")
            machinePoints += 1
            time.sleep(2)

        elif user == 2 and machineOption == "piedra":
            print("La maquina elige: " + machineOption)
            print("Has ganado :) ")
            userPoints += 1
            time.sleep(2)

        elif user == 3 and machineOption == "papel":
            print("La maquina elige: " + machineOption)
            print("Has ganado :)")
            userPoints += 1
            time.sleep(2)

        elif user == 2 and machineOption == "tijeras":
            print("La maquina elige: " + machineOption)
            print("Has perdido :( ")
            machinePoints += 1
            time.sleep(2)

        elif user == 3 and machineOption == "piedra":
            print("La maquina elige: " + machineOption)
            print("Has perdido :( ")
            machinePoints += 1
            time.sleep(2)

        elif user == 1 and machineOption == "tijeras":
            print("La maquina elige: " + machineOption)
            print("Has ganado :) ")
            userPoints += 1
            time.sleep(2)

        attemps += 1
    else:
        print("se han acabado los intentos")
        
        if userPoints > machinePoints:
            print(data[1])
            print("Muy bien, has ganado {} a {}" .format(userPoints, machinePoints))
            print(data[1])
        elif userPoints == machinePoints:
            print(data[1])
            print("has luchado bien y han quedado en empate {} a {}" .format(machinePoints, userPoints))
            print(data[1])
        else:
            print(data[1])
            print("Que mal :( , has perdido {} a {}" .format(machinePoints, userPoints))
            print(data[1])


playGame()
