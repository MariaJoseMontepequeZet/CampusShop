while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar números del 1 al 5")
    print("2. Mostrar tabla de multiplicar")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\nNúmeros del 1 al 5:")
        for i in range(1, 6):
            print(i)

    elif opcion == "2":
        numero = int(input("Ingresa un número: "))
        print(f"\nTabla del {numero}:")
        
        for i in range(1, 11):
            if i == 5:
                continue  # salta el 5
            print(f"{numero} x {i} = {numero * i}")

    elif opcion == "3":
        print("Saliendo del programa...")
        break  # termina el ciclo

    else:
        print("Opción inválida, intenta de nuevo.")