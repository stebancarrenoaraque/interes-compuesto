# programa para determinar el incremento con interes compuesto de un capital

C = int(input("Ingrese el capital inicial: "))

meses = 0
d = C * 2

while (C < d):
    C = C + 0.05 * C
    meses = meses + 1

    print("El capital se duplica en", meses, "meses.")

