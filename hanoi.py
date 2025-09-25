def hanoi(n, origen, auxiliar, destino, paso=1):   # Función recursiva
    if n == 1:                                     # Caso base: solo un disco
        print(f"Paso {paso}: mover disco de {origen} a {destino}")
        return paso + 1                            # Retorna siguiente número de paso
    paso = hanoi(n - 1, origen, destino, auxiliar, paso)  # Mueve n-1 a auxiliar
    print(f"Paso {paso}: mover disco de {origen} a {destino}")  # Mueve disco mayor
    paso = hanoi(n - 1, auxiliar, origen, destino, paso + 1)    # Mueve n-1 sobre el mayor
    return paso                                   # Retorna paso actualizado


if __name__ == "__main__":                        # Punto de entrada del programa
    while True:                                   # Bucle para validar entrada
        try:
            n = int(input("Ingrese el número de discos (1-20): "))
            if 1 <= n <= 20:                      # Rango válido
                break
            print("Debe ser un entero entre 1 y 20.")
        except ValueError:
            print("Ingrese un número entero válido.")

    torres = input("Ingrese nombres de las torres (ej. A B C): ").split()  # Personalización
    if len(torres) != 3: torres = ["A", "B", "C"]   # Si no son 3, usar por defecto

    total = 2 ** n - 1                             # Fórmula movimientos totales
    print(f"\n--- Resolviendo Torres de Hanoi con {n} discos ---")
    hanoi(n, torres[0], torres[1], torres[2])      # Llamada recursiva principal
    print(f"\n Total de movimientos: {total}")   # Resumen final
