# Operadores matemáticos

# Suma

a = 3 ; b = 92.2 ; a1 = 12
print(a+b)
print(a-b)
# Sintaxis reducida 
a1+=2 
print(a1)

# Multiplicación

a = 2 ; b = 34 ; b2= 2
print(a*b)
b2*= 3;
print(b2)
# Sintaxis reducida 

# División int y float

a = 2 ; b = 3 ; a2= 2; a3= 1
print(a/b) # float 
print(a//b) # Int

a2/= 2
a3//= 2

print(a2, a3)
# Sintaxis reducida 

# module (Residuo de la división)

a = 2 ; b = 4 ; x2= 33;
print(a%b);

x2%= 3;
print(x2, "Hola")
# Sintaxis reducida 

# Potencia

a = 2 ; b = 2
print(a**b)
# Sintaxis reducida 

"""
# Codigo ejemplo del Curso
"""

a = "Hola"; b = "¿cómo estás?"; print(a + b) #concatenación de strings;
c = "abc"; print(c*2) # se imprime ese string junto tantas veces se desee
d = 200; d+=10; d-=20; print(d) # es como escribir d = d+10  /  d=d-20
f = 4; f *= 4; print(f) # es como escribir f = f*4
f//=4 ; print(f) # es como escribir f = f//4
f**=2; print(f) # es como escribir f = f**2
f%=2; print(f) # es como escribir f = f%2