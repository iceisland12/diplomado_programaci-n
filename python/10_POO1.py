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


# POO II 

class A: # Clase que tiene dos variables, la cual se define un metodo que imprime las variables
    x = 17 ; y = 6 # estas variables está publicas 
    def imprimir_variables(self):
        print(f'x = {self.x} y = {self.y}')

objeto = A() # Se almacena la class en una variable

objeto.x = 56 ; objeto.y = 12 # Se accede a las variables a través de la variable objeto (No se recomienda hacer esto)
objeto.imprimir_variables() # Se imprime la variable con el metodo imprimir_variable


class B: # Clase que tiene dos variables, la cual se define un metodo que imprime las variables
    __x = 17 ; __y = 6 # Estas variables ya no están públicas.
    def imprimir_variables(self):
        print(f'x = {self.__x} y = {self.__y}')

objeto = B() # Se almacena la class en una variable

objeto.__x = 22 ; objeto.__y = 22 # Al estar privadas, no se pueden acceder y por ende cambiar su valor
objeto.imprimir_variables() # Se imprime la variable con el metodo imprimir_variable


# Tener + de 1 objeto de la misma clase que no sean iguales (Método constructor)

class Personaje:
    def __init__(self, nombre, vida, fuerza):
        self.__nombre = nombre
        self.__vida = vida
        self.__fuerza = fuerza
    
    def mostrar_datos(self):
        print(f'Nombre: {self.__nombre} | Vida: {self.__vida} | Fuerza: {self.__fuerza}')

# Crear instancias de la clase Personaje
a = Personaje('Luis', 1000, 9000)
b = Personaje('Aurora', 1000, 9000)

# Mostrar los datos de los personajes
a.mostrar_datos()
b.mostrar_datos()



# Interacción de una clase con otra 

class Banco:
    def __init__(self, x1): # Constructor de la clase Banco
        self.__dinero = x1
    def boveda(self, x1): # Con este metodo se pude editar la cantidad de dinero del banco
        self.__dinero = x1
    def dinero_del_banco(self): # Se retorna a donde se invoque el metodo la cantidad de dinero del banco
        return self.__dinero

class Ladron:
    __dinero = 0 # Variable privada que representa el dinero del ladrón

    def robar(self, t): # Metodo con el cual se realiza el robo
        self.__dinero += t.dinero_del_banco()
        t.boveda(0)
    def dinero_del_ladron(self): # Metodo que imprime la cantidad de dinero del ladrón
        print('Dinero del Ladrón: ', self.__dinero)

banco1 = Banco(300); ladron1 = Ladron()

ladron1.dinero_del_ladron(); print('Dinero del banco: ', banco1.dinero_del_banco())
ladron1.robar(banco1); print('Robo realizado')
ladron1.dinero_del_ladron(); print('Dinero del banco: ', banco1.dinero_del_banco())


# POO III

# Herencias

'''
Clase Au:
Esta clase tiene un constructor (__init__) que acepta dos argumentos (au y bu).
Dentro del constructor, se inicializan dos atributos de instancia: self.x y self.y, con los valores pasados como argumentos.
Además, hay un método llamado print1 que simplemente imprime el número 1.
'''

class Au:
    def __init__(self,au,bu):
        self.x = au
        self.y = bu
    def print1(self):
        print(1)

'''
Clase Bu (hereda de Au):
La clase Bu hereda de la clase Au. Esto significa que Bu tiene acceso a los atributos y métodos definidos en Au.
Bu tiene dos métodos propios:
datos: Imprime los valores de los atributos self.x y self.y heredados de la clase Au.
print2: Imprime el número 2.
'''


# Los atributos no pueden estar en privados porque si no, no se heredan
class Bu(Au): 
    def datos (self):
        print('Atributos de Herencia: ', self.x, self.y)

    def print2(self):
        print(2)


# objetoAu = Bu('abc', 5); objetoAu.print1() ; objetoAu.print2() ; objetoAu.datos()


# Una clase puede derivar de más de una clase 

class C: 
    def metodo(self, a2):
        print(a2)

'''
Clase C:
Esta clase tiene un método llamado metodo que acepta un argumento a2.
El método simplemente imprime el valor de a2.
'''

class D:
    def __init__(self, t ):
        self.variable = t
    def metodo(self, b1, c):
        print(b1, c)
'''
Clase D:
Esta clase tiene un constructor (__init__) que acepta un argumento t. 
Dentro del constructor, se inicializa un atributo de instancia llamado self.variable con el valor de t. 
Además, hay un método llamado metodo que acepta dos argumentos (b1 y c) y los imprime.
'''

class E(C, D):
    def metodo(self):
        print(self.variable)

'''
Clase E (hereda de C y D): La clase E hereda de las clases C y D. Tiene un método propio llamado metodo1 que imprime el valor del atributo self.variable.
'''
    
objeto = E(16); objeto.metodo()

# Ejemplo II 

# class Persona:
#     def __init__(self, xu, y):
#         self.nombre = xu
#         self.edad = y
#     def saludar(self):
#         print('Hola')
#     def despedirse(self):
#         print('Adios')

# class Profesor(Persona):
#     __asignatura = 'Historia'
#     def datos(self):
#         print(f'Datos del profesor: \n Nombre: {self.nombre} \n Edad: {self.edad} \n Asignatura: {self.__asignatura}')


# persona1 = Profesor('Daniel', 18)
# persona1.saludar()
# persona1.datos()
# persona1.despedirse()

# Segunda sintaxis (De esta Manera el metodo constructor permite agregar la materia sin tener que crear una variable ajuro)

class Persona:
    def __init__(self, xu, y):
        self.nombre = xu
        self.edad = y
    def saludar(self):
        print('Hola')
    def despedirse(self):
        print('Adios')

class Profesor(Persona):
    def __init__(self, a2, b2,c3):
        Persona.__init__(self, a2, b2)
        self.__asignatura = c3
    def datos(self):
        print(f'Datos del profesor: \n Nombre: {self.nombre} \n Edad: {self.edad} \n Asignatura: {self.__asignatura}')

    def datoPriv(self): # Metodo sobre metodo, cuando se declare y se anexe lo valores que pide el constructor deben utilizar este metodo
                        # para que pueda mostrarse el resultado esperado porque está privado!
        self.datos()

# persona1 = Profesor('Daniel', 18, 'Matemática')
# persona1.saludar()
# persona1.datos()
# persona1.despedirse()

persona2 = Profesor('Aurora', 22, 'Farmacia')
persona2.datoPriv()