#6_Funciones

def funcion():
    print('Hoy es un buen día')

funcion()

# 2 ejemplo

# Suma con funciones
    # Argumentos (a,b,c)   
def sumar(a,b,c):
    return(a+b+c)

sumar(2,2,4)
h = sumar(2,5,4)
print(h)

# 3 Ejemplo

a = 5

def sumaArgumento(x):
    x += 7
    print (x)

sumaArgumento(a)


# Ejemplo número enteros desde un punto a a b
def una_funcion(a1, b2):
    print(f"Números enteros desde {a1} hasta {b2}")
    for i in range(a1, b2+1):
        print(i, end=' ')

una_funcion(42, 56)

def suma(x,y):
    return x+y

d = suma(2,3) ; print(d)
# también serviría: print(suma(2,3))