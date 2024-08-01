# 7_Listas


# Las listas se hacen con corchetes separando los elementos por comas

# Ejemplo 1

f = ['True', 4, 99.3, True]
# f es una lista de 4 elementos 
print(f)


# usamos la siguiente sintaxis para acceder a un elemento en especifíco 
# <nombre de la lista >[ posición del elemento ]

a = [1.3, 'a', 3.6]
a1 = a[0] ; a2 = a[2]
print(a1, a2)

b = [2, 33.3, False, "True"]
print(b[2])

# Si queremos hacer un print si los corchetes se hace un ciclo for = 

for i in b:
    print(i, end= '  ')


# Las listas tambien se pueden agregar nuevos elemento con el append() dentro de los parentesis se coloca con lo que se necesite agregar
# Se contenido para una variable o no

a = [] # Lista vacia

b = 5

a.append(b) # Ingresas B
a.append(True)
a.append(4)

print(a)

# Además se puede colocar dentro de los parentesis del .append() un input ya sea con int(input) o float(input)

lista = []
lista.append(int(input("Ingresa un valor a lista: ")))
lista.append((input("Ingresa un valor a lista: ")))
for i in lista:
    print(i, end='  ')

# .pop es para eliminar el ultinmo elemento de la lista

a1 = [6,6.5,"Hola"]
a1.pop()
# v = len(a1)
print(a1)

l = [2,3,4]
suma = 0 
for i in l:
    suma += i
print(suma)