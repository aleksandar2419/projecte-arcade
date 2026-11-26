import robot
import random

def janken():
    el_robot = robot.robot()

    print("\n--- PEDRA, PAPER, TISORA ---")
    print("1. El primer que arribi a 3 victòries")
    print("2. Al millor de 5 rondes")

    mode = ""
    while mode != "1" and mode != "2":
        mode = input("Escull el mode (1 o 2): ")
        if mode != "1" and mode != "2":
            print("Opció no vàlida.")

    punts_jugador = 0
    punts_robot = 0

    print("Mode escollit:", mode)

    while punts_jugador < 3 and punts_robot < 3:
        jugada_jugador = input("Pedra, paper o tisora? ").lower()
        jugada_robot = el_robot.playing()
        print("El robot ha triat:", jugada_robot)

        if jugada_jugador == jugada_robot:
            print("Empat!")
        elif (jugada_jugador == "pedra" and jugada_robot == "tisora") or \
             (jugada_jugador == "tisora" and jugada_robot == "paper") or \
             (jugada_jugador == "paper" and jugada_robot == "pedra"):
            print("Has guanyat la ronda!")
            punts_jugador += 1
        else:
            print("El robot guanya la ronda.")
            punts_robot += 1

        print("Marcador -> Tu:", punts_jugador, "| Robot:", punts_robot)
    

def nana():
    print("Endevina el Número!")
    import random
    secret = random.randint(1, 100)
    intents = 0

    while True:
        intent = int(input("Introdueix el teu intent: "))
        intents += 1

        if intent < secret:
            print("Massa baix!")
        elif intent > secret:
            print("Massa alt!")
        else:
            print(f"Enhorabona! Has endevinat el número en {intents} intents.")
            break