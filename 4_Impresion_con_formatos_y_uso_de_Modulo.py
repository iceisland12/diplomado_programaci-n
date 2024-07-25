# Impresion con formatos y uso de Modulos

# Modulo o librerías 

a = 4; b = 'avion'; c = 222.09

print('A =', a, 'B =', b, 'C =', c)
print('A = {0}, B = {1}, C = {2}'.format(a,b,c)) # Esto indica en la posición (Ya no se usa esto)
print(f'A = {a}, B = {b}, C = {c}') # Manera actual de hacer añadir 
h = f'La Variable A vale: {a} y la B vale: {b}'
print(h)

# %d ---> entero $s ---> str %f ---> float (De esta manera podemos colocar cuando sea el caso)
print('A = %d, B = %s, C = %.3f' % (a,b,c)) 


import math # Se importa libreria
a = math.log2(64); print(f'Logaritmo de base 2 de 64 = {int(a)}') 
b = math.sqrt(625); print(f'Raíz cuadrada de 625: {int(b)}')

import random # Se importa libreria 
a1 = random.randint(1,100); print(a1) # Entero
a2 = random.uniform(1,100); print(a2) # FLoat

from math import sin, fabs, radians # De que liberia "Math" importamos lo que necesitamos (sin,fabs, radians)

s = fabs(5-7); print(int(s), end=' ')
r = sin(radians(45)) ; print(r)