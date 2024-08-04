# 14_EjercicioPractico_04


# Enunciado del problema

# Elaborar un programa que imprima 1 cada vez que el usuario ingrese un numero natural
# que cumpla las siguientes condiciones:

# 	- El numero no debe contener ningun cero como digito
# 	- La suma de los digitos pares debe ser mayor a la suma de los digitos impares

# En caso de que el numero ingresado no cumpla alguna de estas condiciones el usuario
# el programa debe imprimir 0 y esperar a que se ingrese el siguiente numero.

# En caso de que se ingrese un numero negativo, el programa debe tratarlo como uno positivo

# En caso de que el usuario ingrese 0 el programa finaliza

# Ejemplo
# 72
# 0
# 124966		----> suma pares = 2+4+6+6 = 18		suma impares = 1+9 = 10
# 1
# -3
# 0
# 0 				----> finaliza el programa

# def cero(n):
# 	if('0' in str(n)): return True
# 	return False

# def sumapar(n):
# 	k = str(n) ; suma = 0
# 	for i in k:
# 		if(int(i)%2 == 0): suma += int(i)

# 	return suma

# def sumaimpar(n):
# 	k = str(n) ; suma = 0
# 	for i in k:
# 		if(int(i)%2 != 0): suma += int(i)

# 	return suma

# while(True):
# 	n = int(input())
# 	if(n==0): break
# 	if(n<0): n*=-1
# 	if(not cero(n)):
# 		if(sumapar(n)>sumaimpar(n)):
# 			print(1) ; continue
# 	print(0)


def es_numero_natural(numero):
    """
    Verifica si un número es natural (positivo o cero).
    """
    return numero >= 0

def suma_digitos(numero):
    """
    Calcula la suma de los dígitos de un número.
    """
    suma_pares = 0
    suma_impares = 0
    while numero > 0:
        digito = numero % 10
        if digito % 2 == 0:
            suma_pares += digito
        else:
            suma_impares += digito
        numero //= 10
    return suma_pares, suma_impares

def main():
    while True:
        try:
            numero = int(input("Ingrese un número natural (0 para finalizar): "))
            if numero == 0:
                break
            if es_numero_natural(numero):
                suma_pares, suma_impares = suma_digitos(numero)
                if suma_pares > suma_impares:
                    print(1)
                else:
                    print(0)
            else:
                print("Debe ingresar un número natural.")
        except ValueError:
            print("Debe ingresar un número válido.")

if __name__ == "__main__":
    main()
