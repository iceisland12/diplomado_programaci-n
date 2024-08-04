import os
from time import time

class Hanoi:
    def __init__(self):
        self.matriz = []
        self.array = []
        self.l1 = [99999]
        self.l2 = [99999]
        self.l3 = [99999]

    def crear(self):
        self.matriz = []
        self.array = []
        for _ in range(20):
            self.array = [' ' for _ in range(100)]
            self.matriz.append(self.array)

        for i in range(2, 26):
            self.matriz[18][i] = '\u268c'
        for i in range(5, 18):
            self.matriz[i][14] = '\u2503'
        for i in range(36, 60):
            self.matriz[18][i] = '\u268c'
        for i in range(5, 18):
            self.matriz[i][48] = '\u2503'
        for i in range(70, 94):
            self.matriz[18][i] = '\u268c'
        for i in range(5, 18):
            self.matriz[i][82] = '\u2503'

    def menu(self):
        cantidad_discos = 3
        while True:
            os.system('cls')
            print('                          Torres de Hanoi\n\n')
            print('                             Jugar <1>')
            print('                      Cantidad de discos <2>')
            print('\n' * 3)
            x = input()
            self.inicializar_torres()
            
            if x == '1':
                self.llenar_torres(cantidad_discos)
                return cantidad_discos
            elif x == '2':
                while True:
                    cantidad_discos = int(input('Escoja la cantidad de discos con la que quiere jugar (hasta 10): '))
                    if 1 <= cantidad_discos <= 10:
                        break
                self.llenar_torres(cantidad_discos)
                return cantidad_discos

    def inicializar_torres(self):
        self.l1 = [99999]
        self.l2 = [99999]
        self.l3 = [99999]

    def llenar_torres(self, cantidad_discos):
        self.l1 = [99999] + list(range(cantidad_discos, 0, -1))

    def mostrartorres(self, pasos):
        for x in range(20):
            print(''.join(self.matriz[x]))
        print(f'Pasos realizados: {pasos}     reiniciar <4>       menu <5>         salir <6>')

    def colocar_discos1(self, a, cont1, c, b):
        fila = 17
        for x in range(1, cont1):
            t = c - (a[x] - 1)
            q = b + (a[x] - 1)
            for i in range(t, q + 1):
                self.matriz[fila][i] = '\u25A0'
            fila -= 1

    def actualizar_matriz(self):
        self.crear()
        if len(self.l1) >= 2:
            self.colocar_discos1(self.l1, len(self.l1), 12, 16)
        if len(self.l2) >= 2:
            self.colocar_discos1(self.l2, len(self.l2), 46, 50)
        if len(self.l3) >= 2:
            self.colocar_discos1(self.l3, len(self.l3), 80, 84)

    def mover(self, origen, destino):
        if origen[-1] < destino[-1]:
            destino.append(origen.pop())
            self.actualizar_matriz()
            return True
        else:
            print('Movimiento inválido')
            input()
            return False

    def ganar(self, cantidad_discos):
        return len(self.l3) == cantidad_discos + 1 and self.l3[1:] == list(range(cantidad_discos, 0, -1))

    def mensaje(self, tiempo_inicial, tiempo_final):
        tiempo_total = tiempo_final - tiempo_inicial
        print(f'Felicidades, lo has logrado. Su tiempo fue: {tiempo_total:.2f} segundos')
        print('reiniciar <1>   menu <2>   salir <3>')

def main():
    hanoi = Hanoi()
    hanoi.crear()

    while True:
        num_discos = hanoi.menu()
        pasos = 0
        tiempo_inicial = time()

        while True:
            hanoi.mostrartorres(pasos)
            accion = input("Ingrese la torre de origen (1, 2 o 3) o una opción (4: reiniciar, 5: menu, 6: salir): ")
            
            if accion == '4':  # Reiniciar
                break
            elif accion == '5':  # Volver al menú
                break
            elif accion == '6':  # Salir
                return  # Salir del juego completamente

            if not accion.isdigit() or int(accion) not in [1, 2, 3]:
                print("Entrada inválida. Por favor, intente de nuevo.")
                continue

            origen = int(accion)
            destino = int(input("Ingrese la torre de destino (1, 2 o 3): "))
            torres = [hanoi.l1, hanoi.l2, hanoi.l3]
            
            if hanoi.mover(torres[origen-1], torres[destino-1]):
                pasos += 1

            if hanoi.ganar(num_discos):
                tiempo_final = time()
                hanoi.mostrartorres(pasos)
                hanoi.mensaje(tiempo_inicial, tiempo_final)
                opcion = input("Ingrese una opción (1: reiniciar, 2: menu, 3: salir): ")
                if opcion == "1":
                    break  # Reiniciar el juego
                elif opcion == "2":
                    break  # Volver al menú
                elif opcion == "3":
                    return  # Salir del juego completamente
                else:
                    print("Opción no válida. Volviendo al menú principal.")
                    break

        if accion == '6':  # Si se eligió salir durante el juego
            break

if __name__ == "__main__":
    main()