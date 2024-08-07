import random


def generador_palabra_secreta() -> str:
    palabras = ['python', 'javascript', 'java', 'angular',
                'django', 'tensorflow', 'react', 'typescript', 'git', 'flask']
    return random.choice(palabras)


def progreso(palabra_secreta, letras_adivinadas):
    adivinado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado


def ahorcado():
    palabra_secreta = generador_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False
    print("Bienvenido al juego del ahorcado")
    print("Tratá de adivinar la palabra secreta!")
    print(f"Tenés {intentos} intentos")
    print(progreso(palabra_secreta, letras_adivinadas),
          f"La cantidad de letras de la palabra secreta es {len(palabra_secreta)}")

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduzca una letra válida (sólo escribir una letra)")
        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esa letra, prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)
            if adivinanza in palabra_secreta:
                print(f"Muy bien, has acertado! La letra '{
                      adivinanza}' se encuentra en la palabra secreta!")
            else:
                intentos -= 1
                print(f"Que lástima! La letra '{
                      adivinanza}' no se encuentra en la palabra secreta...")
                print(f"Te quedan {intentos} intentos")
        progreso_actual = progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"Felicitaciones has ganado! La palabra secreta era '{
                  palabra_secreta}'")

    if intentos == 0:
        print(f"Se te han acabado los intentos! La palabra secreta era: '{
              palabra_secreta}'")


ahorcado()
