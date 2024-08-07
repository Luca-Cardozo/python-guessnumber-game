import random


def juego_adivinanza():
    print("Bienvenido al juego de adivinanza!")
    print("Trata de adivinar un número del 1 al 99")
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    while adivinado == False:
        intentos += 1
        guess = input("Ingrese un número del 1 al 99: ")
        if guess.isdigit():
            guess = int(guess)

            if guess == numero_secreto:
                adivinado = True
            else:
                print("Fallaste! Inténtalo nuevamente")
                if numero_secreto < guess:
                    print("Prueba con un número menor")
                elif numero_secreto > guess:
                    print("Prueba con un número mayor")
        else:
            print("Error!")
            print("Por favor, ingrese un número del 1 a 99")
    print(f'Felicitaciones! El número era {
          numero_secreto} y lo adivinaste en {intentos} intentos!')


juego_adivinanza()
