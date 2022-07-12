
# Dictionary: Key-Value pairs, Unordered, Mutable

d = {"name": "Manuel", "age": 22, "topic": "ML"}
print(d)

#otra forma:
# d2 = dict(name = "Manuel", age = 22, topic = "ML")
# print(d2)

# Acceder
print(d["name"])
# Nota: si no existe nos manda a error

# Crear nuevo campo
d["weigh"] = 62
print(d)

# elimitar campo
# del d["weigh"]
# ó
# d.popitem() elimina el último item

# try except
if "name" in d:
    print(d["name"])

# or

try:
    print(d["lastname"])
except:
    print("error")

# iterar
for keys in d:
    print(keys)
'''
the same:
for keys in d.keys()
'''

for values in d.values():
    print(values)

# key and value

for key, values in d.items():
    print(key,values,sep=": ")

# copiar dictionarie

d_cpy = d
d_cpy2 = d.copy() # ó d_cpy2 = dict(d)

# no son la misma cosa (ya sabemos por qué)

# merge dos diccionarios:
# d1.update(d2)
# pone los campos que no hay en d1 pero sí en d2

# Mutable:
# accediendo a la key

# se puede usar una tupla como key pero no una lista