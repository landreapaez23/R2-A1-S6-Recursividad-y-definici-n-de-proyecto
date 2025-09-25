def mcd(a: int, b: int) -> int:
    """
    Calcula el Máximo Común Divisor (MCD) de dos números enteros positivos
    usando el algoritmo de Euclides de forma recursiva.

    Caso base:
        - Si b == 0, entonces el MCD es a.
    Caso recursivo:
        - Si b != 0, el problema se reduce a calcular:
          MCD(a, b) = MCD(b, a % b)

    Parámetros:
        a (int): Primer número.
        b (int): Segundo número.

    Retorna:
        int: El MCD de a y b.
    """
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


def solicitar_numero(mensaje: str) -> int:
    """
    Solicita un número entero positivo al usuario con manejo de errores.
    Repite hasta que el usuario ingrese un valor válido.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print(" Error: debe ingresar un número entero POSITIVO.")
            else:
                return valor
        except ValueError:
            print(" Error: debe ingresar un número válido (entero).")


def main():
    print("=== Cálculo del Máximo Común Divisor (MCD) ===")

    # Pedir números con validaciones
    a = solicitar_numero("Ingrese el primer número entero positivo: ")
    b = solicitar_numero("Ingrese el segundo número entero positivo: ")

    # Calcular y mostrar resultado
    print(f"El MCD de {a} y {b} es {mcd(a, b)}")


if __name__ == "__main__":
    main()

