# Manera 1 de agregar texto pero que se borrará y actualizará 

# a = open('9_ejemplo.txt', 'w+')
# a.write('Hola!\n')
# a.close()


# Manera 2 de agrega y de que se quede el contenido previo 
# a = open('9_ejemplo2.txt', 'a')
# a.write('Hola esto se añade al contenido anterior \n')
# for x in 'ABCDEFG':
#     a.write(x + '\n')


# Manera 3: Manejo de Archivos de texto

a = open('9_Ejemplo2.txt', 'r')
print(a.read()); a.seek(0) # se usa esta función cuando necesitamos que lea el archivo más de una vez (a.seek(0)) ---> el 0 dice la posición inicial de contenido del texto 
print(a.read());
a.close()

a = open('foo.txt', 'w')
for i in range(1,6):
    a.write(str(i))

a = open('9_foo2.txt' , 'w')
for i in range(1,6):
    a.write(str(i))