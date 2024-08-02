# 10_POO

# Paradigma Programación Orientada a Objeto (POO)
# Paradigmas Vistos: Condicionales ---> ciclos ---> Progrmación Estructurada
# Funciones ---> Programación Modular 
# Funciones de una clase ---> Metodos


a = "Murcielago"
print(a.upper()) # Poner en mayúsculas. .upper es un metodo que a su vez a es un objeto que tiene un metodo STR

b = 'ABC' # del b # Se borra antes de imprimir el valor 
print(b.lower()) # Poner en minúsculas. .lower es un metodo que a su vez a es un objeto que tiene un metodo STR

# Crear clases con sus propios metodos

class persona: # Se usa palabra reservada class para elaborar una clase.
    edad = 20
    dinero = 500

    def saludar (self):
        print('Hola')
    def despedirse (self):
        print('Adios.')
    def vender(self):
        self.dinero+= 200
    def mostra_dinero_actual(self):
        print(self.dinero)
    def quiebra(self):
        self.dinero = 0

a = persona()
a.saludar()
a.despedirse()

a.vender() ; a.mostra_dinero_actual()
a.quiebra() ; a.mostra_dinero_actual() 

# Imprimer variables usando el metodo aunque no se debe usar tan libremente en los atributos
x = persona()
x.edad = 14  # <<<<<<<<<<<<<<<<<         No se debe hacer                                      >>>>>>>>>>>>>>>>>>>>>>>
print(x.edad)