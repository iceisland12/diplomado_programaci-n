# 5_ciclos

# Existen dos ciclos while y for , se hacen para ahorrar tiempo

# i = 1
# while(1<=10):
#     print(i, end='  ') # end= '  ' marca la distancia entre lo números en el print
#     i += 1

# Ejemplo 2

# range(5) ---> 0,1,2,3,4 (Empieza a contar desde el 0 hasta el 4)
# range(1,6) ---> 1,2,3,4,5 (Emepiza a contar desde el 1 hasta el 5, el utltimo rango es el 5 )
# range(1, 11, 2) ---> 1,3,5,7,9  (3 argumnentos generan un )

# Ejemplo for 

for i in range (1,11):
    print(i, end='   ')

# Ejemplo 4 imprimir variables en ciclo for
a = 'abcdefg'

for i in a: # donde i (variable que acumula el ciclo) dentro de a (variable que contiene el str):
    print(i, end='  ') # Imprime i , con está separación

