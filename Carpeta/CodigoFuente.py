import os
from time import time
matriz = []; array=[]
def crear():
        global matriz; global array
        matriz = []; array=[]
        for x in range(20):
            for i in range(100):
                array.append(' ')
            matriz.append(array); array=[]

        for i in range(2,26):       #base
            matriz[18][i]='\u268c'    

        for i in range(5, 18):
            matriz[i][14]='\u2503'

        for i in range(36,60):
            matriz[18][i]='\u268c'    #base 

        for i in range(5, 18):
            matriz[i][48]='\u2503'

        for i in range(70,94):
            matriz[18][i]='\u268c'    #base 

        for i in range(5, 18):
            matriz[i][82]='\u2503'
crear()

def mostrartorres(p):
    global matriz; global array
    for x in range(20):
        for i in range(100):
            if(i==99): print(matriz[x][i]); continue
            print(matriz[x][i], end='')
    print('Pasos realizados :', p,'     reiniciar <4>       menu <5>         salir <6>')



def mostrar(a,b,c):
    for i in a:
        print(i, end=' ')
    print("")
    for i in b:
        print(i, end=' ')
    print("")
    for i in c:
        print(i, end=' ')
    print("")


def ganaste(c, cantidad_discos):
    if(not len(c)==cantidad_discos+1): return False
    for i in range(cantidad_discos):
        if( not c[i+1]==cantidad_discos-i): return False
    return True


l1=[]; l2=[]; l3=[]

def llenar_torres(cantidad_discos):
    for i in range(cantidad_discos):
            l1.append(cantidad_discos-i)

def inicializar_torres():
    global l1; global l2; global l3;
    l1=[99999]; l2=[99999]; l3=[99999]
  

def menu():
    cantidad_discos=3; global l1; global l2; global l3
    for i in range(4): print('')
    while(True):
        os.system('cls')
        print('                          Torres de Hanoi'+'\n'*2)
        print('                             Jugar <1>')
        print('                      Cantidad de discos <2>')
        for i in range(3): print('')
        x=input()
        inicializar_torres()
        
        if(x=='1'): 
            llenar_torres(cantidad_discos)
            return cantidad_discos
        elif(x=='2'):
            while(True):
                cantidad_discos=int(input('Escoja la cantidad de discos con la que quiere jugar (hasta 10): '))
                if( not cantidad_discos<1 and not cantidad_discos>10): break
            llenar_torres(cantidad_discos)
            return cantidad_discos
        

def colocar_discos1(a, cont1, c, b):
    global matriz
    
    t=0; q=0 ; fila=17; 
    for x in range(1,cont1):
            if(a[x]==1): t=c; q=b 
            elif(a[x]==2): t=c-1; q=b+1
            elif(a[x]==3): t=c-2; q=b+2
            elif(a[x]==4): t=c-3; q=b+3
            elif(a[x]==5): t=c-4; q=b+4
            elif(a[x]==6): t=c-5; q=b+5
            elif(a[x]==7): t=c-6; q=b+6
            elif(a[x]==8): t=c-7; q=b+7
            elif(a[x]==9): t=c-8; q=b+8
            else: t=c-9; q=b+9
            for i in range(t,q+1):
                matriz[fila][i]='\u25A0'
            fila-=1
    



def last(a):
    return (a[len(a)-1])

def actualizar_matriz():
        global l1; global l2; global l3
        matriz = []; array=[]
        crear()
        if(len(l1)>=2): colocar_discos1(l1, len(l1), 12, 16)
        if(len(l2)>=2): colocar_discos1(l2, len(l2), 46, 50)
        if(len(l3)>=2): colocar_discos1(l3, len(l3), 80, 84)
        
                


def mover(a,b):
        if(last(a) < last(b)):
            b.append(last(a)); a.pop()
            actualizar_matriz()
        else:
            print('movimiento invalido')
            x=input()

def mover1_2():
    global l1; global l2
    mover(l1,l2)

def mover1_3():
    global l1; global l3
    mover(l1,l3)

def mover2_3():
    global l2; global l3
    mover(l2,l3)

def mover2_1():
    global l2; global l1
    mover(l2,l1)

def mover3_1():
    global l3; global l1
    mover(l3, l1)

def mover3_2():
    global l3; global l2
    mover(l3, l2)

def colocar_discos(a):
    colocar_discos1(l1, a+1, 12, 16)

def ganar(a):
    return ganaste(l3, a)

def Inicializar_torres(cantidad_discos):
    inicializar_torres()
    llenar_torres(cantidad_discos)

def mensaje(a,b):
    print('Felicidades, lo has logrado.  Su tiempo fue: %.2f segundos' % (b-a) )
    print('reiniciar <1>   menu <2>   salir <3>')