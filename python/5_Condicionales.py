# 5_Condicionales

# Toda sentencia de condicional es el if
# Se debe resptar las sangrias aunque se pueden escribir las instrucciones al lado

a = input('Ingrese un valor númerico sin decimales: ')

# if(2+2 == 4):
#     print(1)

if(2-2 == 0):
    print(f'Es igual a = {a}')

# if con else: solo se ejuecuta si el condicional anterior es false
a = int(input('Ingrese el número para saber si es par o no: '))
if(a%2 == 0): # a%2 Es saber si el cociente es 0 al final de la división
    print(f'El valor que ingresaste ({a}) es par')
else:
    print('Es impar')

# Elif 

a = input('Ingrese una letra: ')
if (a == 't'):
    print('Es la letra t, el valor que ingresaste')
elif (a == 's'):
    print('Es la letra S, el valor que agregaste')
elif (a == 'j'):
    print('Es la letra J, el valor que agregaste')
else:
    print('No es la letra que se busca')

    # Actualización PC


a1 = input('Ingrese un número: ')
if (a1 == 2):
    print ('Es el número ganador')
elif (a1 == 3):
    print ('Es el número de empate')
else:
    print('Lo siento perdiste')