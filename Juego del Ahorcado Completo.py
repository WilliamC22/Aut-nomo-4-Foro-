
import random

ahorcado_dibujos = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    ========='''
]   


def obtener_palabra():
    palabras = ["gato", "perro", "casa", "arbol", "coche"] # Lista de palabras predefinidas
    palabra_personalizada = input("Ingresa una palabra personalizada (o presiona Enter para usar una palabra aleatoria): ")
    if palabra_personalizada:
        return palabra_personalizada.lower()
    else:
        return random.choice(palabras)

def jugar_ahorcado():
    palabra = obtener_palabra()
    palabra_adivinada = "_" * len(palabra)
    intentos_restantes = 6
    letras_adivinadas = []

    while intentos_restantes > 0 and "_" in palabra_adivinada:
        print(ahorcado_dibujos[intentos_restantes])
        print("\nPalabra: " + " ".join(palabra_adivinada))
        print("Intentos restantes: " + str(intentos_restantes))
        print("Letras adivinadas: " + ", ".join(letras_adivinadas))

        letra = input("\nIngresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. ¡Intenta con otra!")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            indices = [i for i, l in enumerate(palabra) if l == letra]
            for indice in indices:
                palabra_adivinada = palabra_adivinada[:indice] + letra + palabra_adivinada[indice+1:]
        else:
            print("Letra incorrecta.")
            intentos_restantes -= 1

    if "_" not in palabra_adivinada:
        print("\n¡Felicidades! Has adivinado la palabra: " + palabra)
    else:
        print("\n¡Oh no! Has agotado tus intentos. La palabra era: " + palabra)

jugar_ahorcado()