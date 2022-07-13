# itertools:  product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

# the product of the items
a = [1,2]
b = [3,4]
p = product(a,b)
print(list(p))

# p = product(a,b, repeat=2) -> número de veces para hacer el producto

# permutations, return all the orderings possibiles

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

# permutations(a,2) -> especificar el orden de la permutación


# combinations: make all possibles combinations with specified length

comb = combinations(a, 2)
print(list(comb))

# combinations with replacement

comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

# accumulate

# la suma acumulada:
acc = accumulate(a)
print(list(acc))

# acc = accumulate(a, func=max)

def smaller_than_3(x):
    return x < 3
# groupby

gb = groupby(a, key=smaller_than_3)
for key, value in gb:
    print(key,list(value))

# con lambda
# key=lambda x: x<3 (trick)

# count, cycle, repeat

for i in count(10):
    print(i)
    if (i == 15):
        break

for i in cycle(a):
    print(i)

for i in repeat(1, 10):
    print(1)