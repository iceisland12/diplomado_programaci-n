#11_Ejercicio_programación_01

#Crear un programa que cuente cuantas veces aparece cierto caracter en un string.

# El usuario primero ingresara un numero entero que indicara las veces en que necesita usar el programa. (numero de iteraciones)
# En cada iteracion el usuario primero ingresara un string (cadena de caracteres) y luego en la siguiente linea un caracter.
# Cuando se termine de ingresar la entrada, el debera atender cada caso en el orden ingresado
# Indicando cuantas veces aparece tal caracter en la cadena asignada, en esa cadena no se debe mostrar en la salida
# Sino que se debe referir a ella, mostrando el su posicion en la entrada.


# Ejemplo: 
# 2						------> numero de casos
# abcc
# c
# 1245
# 3
# En la cadena de caracteres #1 el caracter 'c' aparece 2 veces     ------> empieza la salida
# En la cadena de caracteres #2 el caracter '3' aparece 0 veces


x = int(input("Ingrese el valor en números: ")); lista1 = [] ; lista2 = []
for i in range(x):
    string = input("Ingrese el valor en letras: ")
    lista1.append(input("Ingrese el valor en letras: "))
    
    if(lista1[i] in string):
        cont = 0 
        for a in string:
            if(a == lista1[i] ): 
                cont+= 1 
        lista2.append(cont)
    else: lista2.append(0)
        
for i in range(x):
    print(f'En la cadena de caracteres #{i+1} el caracter {lista1[i]}, aparece {lista2[i]} veces.' )

    '''
    Entrada de datos:
1. El usuario ingresa un número entero x, que representa la cantidad de casos que se evaluarán.
2. Luego, para cada caso, ingresa una cadena de caracteres (string) y el carácter que desea buscar en esa cadena (lista1[i]).

    Procesamiento:
        Para cada caso:
            1. Verificas si el carácter ingresado (lista1[i]) está presente en la cadena (string).

Si está presente:
    1. Inicializas un contador (cont) en 0.
    2. Recorres cada carácter en la cadena (for a in string).
    3. Si el carácter actual (a) es igual al carácter buscado (lista1[i]), incrementas el contador.
    4. Almacenas el valor del contador en lista2.
    5. Si no está presente, agregas 0 a lista2.
    
    Salida:
    1. Finalmente, muestras los resultados para cada caso.
    2. Imprimes un mensaje que indica la cadena de caracteres evaluada, el carácter buscado y la cantidad de veces que aparece en esa cadena.
    '''


x = int(input("Ingrese el número de casos: "))
lista1 = []
lista2 = []

for i in range(x):
    string = input(f"Ingrese la cadena de caracteres #{i+1}: ")
    caracter = input("Ingrese el caracter a buscar: ")
    
    if caracter in string:
        cont = 0
        for a in string:
            if a == caracter:
                cont += 1
        lista2.append(cont)
    else:
        lista2.append(0)

for i in range(x):
    print(f"En la cadena de caracteres #{i+1}, el caracter '{caracter}' aparece {lista2[i]} veces.")
