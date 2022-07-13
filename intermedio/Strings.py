
str = "Hola mundo"
# str = 'Hola mundo'

#cualquiera de las dos son válidas

'''
Trabajar con multiples líneas
str = """"Hello
World"""

# poner una / anula el salto de línea
'''

char = str[0]
print(char)
print(type(char))

# no sporta item mutable

# substr

print(str[5:10])

# mismas reglas de slicing

# concatenación de strings:
sentences = "hello" + " world"

# iteración:
for i in sentences:
    print(i, end="")

if "hello" in sentences:
    print("\nyes\n")

# remove white space
s = sentences.strip()
print(s)

# Fancy funct:
str.lower()
str.upper()
str.startswith("Hola")
str.endswith("Mundo")
str.find('o') #return de index
str.count('o')
str.replace('World', 'Mundo')

# string and list
# separa las palabras
lst = str.split() # el argumento es el delimitador

# concatenar elemenos de la lista
# es más limpio para concatenar que utilizar un for +=
concat = ' '.join(lst)

# %, .format(), f-strings

s = "%s" % str
print(s)

var = 2
print("%d" % var)

print("{} and {:.2f}".format("hola mundo", 12.2))

# f-strings
print(f"hola {var}")





