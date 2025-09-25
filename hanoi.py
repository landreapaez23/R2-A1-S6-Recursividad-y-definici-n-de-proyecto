"""
Torres de Hanoi - Implementación recursiva con validaciones y personalización de torres.
"""

from typing import List


def hanoi(
    n: int,
    origen: str,
    auxiliar: str,
    destino: str,
    movimientos: List[str],
    paso: int = 1,
) -> int:
    """
    Resuelve el problema de las Torres de Hanoi recursivamente.

    Parámetros:
        n (int): Número de discos.
        origen (str): Torre de origen.
        auxiliar (str): Torre auxiliar.
        destino (str): Torre destino.
        movimientos (List[str]): Lista para registrar los movimientos.
        paso (int): Contador de pasos (por defecto 1).

    Retorna:
        int: Último número de paso utilizado.
    """
    if n == 1:
        movimientos.append(f"Paso {paso}: mover disco desde {origen} hacia {destino}")
        return paso + 1
    else:
        paso = hanoi(n - 1, origen, destino, auxiliar, movimientos, paso)
        movimientos.append(f"Paso {paso}: mover disco desde {origen} hacia {destino}")
        paso += 1
        paso = hanoi(n - 1, auxiliar, origen, destino, movimientos, paso)
        return paso


def pedir_numero_discos() -> int:
    """Solicita al usuario un número de discos válido (1–20)."""
    while True:
        try:
            n = int(input("Ingrese el número de discos (1–20): "))
            if 1 <= n <= 20:
                return n
            else:
                print(" Error: El número debe estar entre 1 y 20.")
        except ValueError:
            print(" Error: Ingrese un número entero válido.")


def pedir_nombres_torres() -> tuple[str, str, str]:
    """
    Solicita los nombres de las torres al usuario.
    Si se dejan vacíos, se asignan valores por defecto (A, B, C).
    Se valida que los nombres no estén repetidos.
    """
    while True:
        origen = input("Nombre de la torre de origen (por defecto A): ") or "A"
        auxiliar = input("Nombre de la torre auxiliar (por defecto B): ") or "B"
        destino = input("Nombre de la torre destino (por defecto C): ") or "C"

        nombres = {origen, auxiliar, destino}
        if len(nombres) < 3:
            print(" Error: Los nombres de las torres deben ser distintos.")
            continue
        return origen, auxiliar, destino


def main() -> None:
    """Función principal que ejecuta el programa."""
    print(" Torres de Hanoi - Versión Recursiva\n")

    n = pedir_numero_discos()
    origen, auxiliar, destino = pedir_nombres_torres()

    movimientos: List[str] = []
    hanoi(n, origen, auxiliar, destino, movimientos)

    for mov in movimientos:
        print(mov)

    print(f"\n Total de movimientos esperados: {2 ** n - 1}")


if __name__ == "__main__":
    main()
