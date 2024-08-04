# 13_ejercicio_practico_03


# Enunciado
# Dado un archivo de texto, llamado "matrices.txt", donde estan escritas
# una serie de matrices de numero enteros, crear un archivo de texto
# llamado "salida.txt", en donde se indique el número mayor de cada matriz mostrada en el archivo.

# el archivo "matrices.txt" estará en el mismo directorio que el código fuente.


#  Ejemplo;
# 1
# 2
# 1 4
# 2 1
# numero mayor de la matriz #1: 4


# archivo1 = open("matrices.txt", "r")
# archivo2 = open("salida2.txt", "w")
# n = int(archivo1.readline())
# t = 0; l = []
# for i in range(n):
# 	dimension = int(archivo1.readline())
# 	for i2 in range(dimension):
# 		l = list(archivo1.readline().split())
# 		for i3 in l:
# 			if(int(i3)>t): t = int(i3)
# 	archivo2.write(f"numero mayor de la matriz #{i+1}: {t} \n"); t = 0

# archivo1.close(); archivo2.close()


# Optimización de codigo

archivo1 = open("matrices.txt", "r")
archivo2 = open("salida12.txt", "w")
n = int(archivo1.readline())

for i in range(n):
    dimension = int(archivo1.readline())
    t = 0  # Reiniciar t para cada matriz
    for _ in range(dimension):
        l = list(map(int, archivo1.readline().split()))
        for i3 in l:
            if i3 > t:
                t = i3
    archivo2.write(f"Número mayor de la matriz #{i+1}: {t}\n")

archivo1.close()
archivo2.close()

print("Resultados escritos en salida1.txt")



# Ver cual matriz es mayor

# def leer_matrices(nombre_archivo):
#     """
#     Lee las matrices desde un archivo de texto y devuelve una lista de matrices.
#     """
#     matrices = []
#     with open(nombre_archivo, "r") as archivo:
#         matriz_actual = []
#         for linea in archivo:
#             if linea.strip():  # Ignorar líneas vacías
#                 fila = list(map(int, linea.split()))
#                 matriz_actual.append(fila)
#             else:
#                 matrices.append(matriz_actual)
#                 matriz_actual = []
#         if matriz_actual:
#             matrices.append(matriz_actual)
#     return matrices

# def encontrar_maximo(matriz):
#     """
#     Encuentra el número máximo en una matriz.
#     """
#     maximo = float("-inf")
#     for fila in matriz:
#         maximo = max(maximo, max(fila))
#     return maximo

# def escribir_resultados(matrices, nombre_archivo_salida):
#     """
#     Escribe los resultados en un archivo de salida.
#     """
#     with open(nombre_archivo_salida, "w") as salida:
#         for i, matriz in enumerate(matrices, start=1):
#             maximo = encontrar_maximo(matriz)
#             salida.write(f"Número mayor de la matriz #{i}: {maximo}\n")

# def main():
#     nombre_archivo_entrada = "matrices.txt"
#     nombre_archivo_salida = "salida.txt"
#     matrices = leer_matrices(nombre_archivo_entrada)
#     escribir_resultados(matrices, nombre_archivo_salida)
#     print(f"Resultados escritos en {nombre_archivo_salida}")

# if __name__ == "__main__":
#     main()

