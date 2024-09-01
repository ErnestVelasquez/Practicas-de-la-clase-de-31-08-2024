filas = int(input("Ingresa el numero de filas:"))
columnas = int(input("Ingresa el numero de columnas: "))

matriz = [["A" for _ in range(columnas)] for _ in range(filas)]

print("\nLa matriz rasultante es:")
for fila in matriz:
    print(fila)