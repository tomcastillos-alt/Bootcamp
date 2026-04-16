# Ejercicio 1. Imprime números del 0 al 100
for numero in range(101):
    print(numero)


# Ejercicio 2. Números pares
for numero in range(2, 501, 2):
    print(numero)


# Ejercicio 3.  Ice Ice Baby
for numero in range(1, 101):
    if numero % 10 == 0:
        print("baby")
    elif numero % 5 == 0:
        print("ice ice")
    else:
        print(numero)


# Ejercicio 4. Wow. Número gigante a la vista
suma_pares = sum(range(0, 500001, 2))
print(suma_pares)


# Ejercicio 5. Regrésame al 3
numero = 2024
while numero > 0:
    print(numero)
    numero -= 3


# Ejercicio 6. Contador dinámico
numInicial = 3
numFinal = 10
multiplo = 2

for numero in range(numInicial, numFinal + 1):
    if numero % multiplo == 0:
        print(numero)