
# Paréntesis son opcionales
# Si hay sólo un elemento se pone una "coma"al final
t = ("Manuel", 22, "ML")
print(t)

# Poder saber el tipo de elemento con type
print(type(t))

# Podemos crear una tupla desde una lista
from_list = tuple(["Manuel", 22, "ML"])

# Para acceder a un elemento se puede desde indice
# Indices negativos es el orden inverso de indice positivo
# t[2] igual a t[-1]

# La tupla NO SE PUEDE MODIFICAR UNMUTABLE

# Iterar sobre la tupla

for i in t:
    print(i, end=",")

# chechar si está dentro

if "Manuel" in t:
    print("yes")

#Longitud
len(t)

# números de un elemento
t.count("Manuel")

# el primer indice de un elemento
t.index("Manuel")
# si el elemento no está manda un error

# tuple to list
tuple_to_list = list(t)

# Slicing

a = 1,2,3,4,5
b = a[2:4] # ultimo no se toma en cuenta
print(b)

# si no se especifica el primero, inicia desde el inicio
# si no se especifica el tope, llega al final
# ::2 elementos pares, etc
# tricky ::-1 reverse

#unpacket
#tienen que ser los valores excactos
name, age, topic = t
print(name)
# asterísco sirve para generalizar
#example
a, *b = t
print(b)

#tupla es más optimizada que la lista, en tiempo y espacio