import jocs
def mostrar_menu():
    print("\n--- BENVINGUT/DA AL MINI ARCADE ---")
    print("1. Jugar a Pedra, Paper, Tisora")
    print("2. Jugar a Endevinar el Número")
    print("S. Sortir\n")

while True:
    mostrar_menu()
    opcio = input("Selecciona una opció: ").upper()
    if opcio == "1":
        jocs.janken()
    elif opcio == "2":
        jocs.nana()
    elif opcio == "S":
        print("Adéu! Gràcies per jugar.")
        break
    else: print("Opció no valida")