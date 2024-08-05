# 8_lectura_de_archivos_de_Texto

# Manera 1 de colocarlo

a = open('8_foot.txt', 'r')
# print(a.read())
# a.close()


# Manera 2 (Se graba en una variable para que la lea luego se imprime y se cierra)
a1 = a.read()
print(a1)
a.close()


# Manera 3  con rutas (Se coloca una r'para evitar errores en la ruta' )
ruta = r'C:\Users\luisg\Desktop\Cursos\diplomado_programación\8_archivo.txt'

archivo2 = open(ruta, 'r')
print(archivo2.read())
archivo2.close()


# Manera 4 la cual está en nuestro mismo directory con el ciclo for

# archivo3 = open('8_archivo2.txt', 'r')

# for linea in archivo3:
#     if(linea == '1\n' or linea == '0\n'): continue # Evalua la variable linea, si linea es igual al string 1 o 0 que tenga un salto de línea se ejecuta y se imprime
#     print(linea)

# Manera que quitara los saltos de lineas
archivo4 = open('8_archivo2.txt', 'r')

for linea in archivo4:
    if (linea == '1\n' or linea == '0\n' or linea == '0'):
        continue  # Evalúa la variable "linea". Si "linea" es igual al string "1" o "0" con un salto de línea, se ejecuta y se imprime.
    print(linea.strip('\n'))
