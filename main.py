import random

rng = random.randint(1, 20)

while True:  
    print("Introduzca un numero")
    
    try:
        numeroIntroducido = int(input())
    except ValueError:
        print("Por favor, introduce un numero valido.")
        continue 

    if rng == numeroIntroducido:
        print(f"Enhorabuena! Adivinaste el numero, era {rng}. Deseas continuar? (S/N)")
        continuar = input().strip().upper()
        if continuar == "S":
            rng = random.randint(1, 20)  
            continue
        else:
            print("Gracias por jugar.")
            break
    elif numeroIntroducido > rng:
        print("El numero es menor")
    else:
        print("El numero es mayor")