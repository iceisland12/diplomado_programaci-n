# 16_Optimización.py

# from time import time

# t1 = time()


# #Algoritmo principal
# a = open('Entrada1.txt', 'r')
# l = []
# for line in a:
# 	suma = 0; p = line.strip('\n')
# 	for i in p:
# 		suma += int(i)

# 	if(suma == 36): l.append(int(p))

# l.sort()
# print(l[len(l)-1])


# t2 = time()
# print(t2 - t1)

from time import time

t1 = time()

# Algoritmo principal
a = open('Entrada1.txt', 'r')
l = []

for line in a:
    suma = 0
    p = line.strip('\n')

    for i in p:
        suma += int(i)

    if suma == 36:
        l.append(int(p))

l.sort()

if l:
    print(l[-1])  # Imprime el último elemento de la lista (mayor número)
else:
    print("No se encontraron números que cumplan las condiciones.")

t2 = time()
print("Tiempo de ejecución:", t2 - t1)
