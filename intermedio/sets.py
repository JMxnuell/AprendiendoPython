
# Sets: unordered, mutable, no duplicates

# se crea como diccionario pero sin keys
myset = {3, 0, -2, -2, -1}
print(myset)

# orden arbitrario

# myset = { } reconoce como list
# por lo tanto debería de ser myset = set()

myset.add(1)
print(myset)

# remove
myset.remove(-2)
# error if don't find it

# discard
myset.discard(-2)
# no hay error
print(myset)

# myset.clear()
# myset.pop()

for i in myset:
    print(i, end=", ")

if 1 in myset:
    print("\nyes it is")

# Unir dos o más sets

odds = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
t = odds.union(even)
print(t)

# Intersección:

print(t.intersection(odds))

# Difference
print(t.difference({1, 2, 3}))

# Difference in both sets
print(t.symmetric_difference({1, 2, 3, 11, 12}))

# Añade los elementos que no se encuentren en el set
# Union entre los dos sets
t.update({13, 14})

# Update the set with the interesecction
t.intersection_update({1, 2, 3})

# Update the set with the difference
t.difference_update({1, 2, 3})
# Update the set with the simetric difference
t.symmetric_difference_update({1, 2, 3})

# Otros métodos:
# issubset(set)
#  issuperset(set)
# isdisjoint(set)

# Para una copia el mismo principio que con listas...

# set estático
a = frozenset(t)
print(a)

