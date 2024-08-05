# Conversión de Tipos de Datos

int() # convierte a entero (Valores sin decimales)
float() # Convierte a flotante  (Valores con decimales)
str() # Convierte a string (Cadenas de texto)
bool() # Convierte a verdadero o falso


a = int(4566.12); print(a) ; a1 = 5 ; b2 = 62.5; c = float(a1); print(c)# Ejemplo 1
b = float(4562); print(b); a1 = 5 ; b2 = 62.5; c = int(b2); print(c) # Ejemplo 2
c = str(); print(c) # Ejemplo 3
d = bool(0); e = bool('Hola'); print(d,e) # Ejemplo 4: 0 = false y 1 = True
f = 'holahola'; print(f[0])

a = 18.1039; a = int(a)
print(a); print(float(a))
b ="340"; b = int(b)
b = b+a
print(b)
c = 34; c = str(c)
print(c+'texto')

g = '1o3aquis'
print(int(g[0]) + int(g[2]))

a2 = 2; a3 = 4

c = str(a2) + str(a3)
print(c)
