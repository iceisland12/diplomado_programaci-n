#12_ejercicio_práctico_02

# Enunciado:

# Elaborar un programa detector de números primos

# Recordemos que un número primo es un número natural que sólo es divisible entre 1 y él mismo

# Ejemplo de números primos: 13, 97, 19, 2

# Entrada:

# El usuario primero ingresará un número indicando la cantidad de números con los que trabajará el programa

# Luego, linea por linea se ingresará los números

# Salida:

# Finalmente en la salida se debe indicar cuál número es primo (en caso de haber) y cual es compuesto.
# En el orden inverso a como se ingresaron

# Ejemplo:

# 3
# 2
# 4
# 5
# 5 es primos				---> el último numero ingresado es el primero en la salida
# 4 es compuesto
# 2 es primo



class A:
    def __init__(self, n):
        self.numeroDeCasos = n
        self.lista = []
    
    def pedirNumero(self):
        for i in range(self.numeroDeCasos):
            self.lista.append(int(input("Ingrese un número: ")))

    def salida(self):
        while(True):
            x = self.lista[self.numeroDeCasos - 1] ; primo = True

            for i in range (2,x):
                if ( x%i == 0 ): 
                    primo = False
                    print(f'{x} es compuesto'); break 
            if(primo):
                print(f'{x} es primo.')
            self.numeroDeCasos-= 1
            if(self.numeroDeCasos == 0):
                break
            

a = A(int(input("Ingrese la cantidad de números a evaluar: ")))
a.pedirNumero()
a.salida()

# class A:
#     def __init__(self, n):
#         self.numeroDeCasos = n
#         self.lista = []
    
#     def pedirNumero(self):
#         for i in range(self.numeroDeCasos):
#             self.lista.append(int(input("Ingrese un número: ")))

#     def salida(self):
#         while True:
#             x = self.lista[self.numeroDeCasos - 1]
#             primo = True

#             for i in range(2, int(x**0.5) + 1):
#                 if x % i == 0:
#                     primo = False
#                     print(f"{x} es compuesto")
#                     break

#             if primo:
#                 print(f"{x} es primo.")

#             self.numeroDeCasos -= 1
#             if self.numeroDeCasos == 0:
#                 break

# a = A(int(input("Ingrese la cantidad de números a evaluar: ")))
# a.pedirNumero()
# a.salida()