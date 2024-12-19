import random

def jugar_ahorcado():
    # Lista de palabras para el juego
    palabras = ["viajar","carro", "nevera"]
    palabra_secreta = random.choice(palabras).lower()
    letras_adivinadas = ["_"] * len(palabra_secreta)
    intentos_restantes = 3
    letras_usadas = []

    print("¡Bienvenido al juego del Ahorcado!")
    print("Adivina la palabra: " + " ".join(letras_adivinadas))

    # Ciclo principal del juego
    while intentos_restantes > 0 and "_" in letras_adivinadas:
        print(f"\nIntentos restantes: {intentos_restantes}")
        print(f"Letras usadas: {', '.join(letras_usadas)}")
        print("Palabra actual: " + " ".join(letras_adivinadas))

        # Solicitar una letra al usuario
        letra = input("Ingresa una letra: ").lower()

        # Validar entrada
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una letra válida.")
            continue

        if letra in letras_usadas:
            print("Ya has usado esa letra. Intenta con otra.")
            continue

        # Agregar la letra a las usadas
        letras_usadas.append(letra)

        # Verificar si la letra está en la palabra secreta
        if letra in palabra_secreta:
            print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
            for i, l in enumerate(palabra_secreta):
                if l == letra:
                    letras_adivinadas[i] = letra
        else:
            print(f"La letra '{letra}' no está en la palabra.")
            intentos_restantes -= 1

    # Fin del juego
    if "_" not in letras_adivinadas:
        print("\n¡Felicidades! Adivinaste la palabra:", palabra_secreta)
    else:
        print("\n¡Perdiste! La palabra era:", palabra_secreta)

# Ejecutar el juego
if __name__ == "__main__":
    jugar_ahorcado()


