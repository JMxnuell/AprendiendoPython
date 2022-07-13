
# lambda arguments: expression
from functools import  reduce
add10 = lambda x: x + 10
print(add10(5))

mult = lambda x, y:  x * y
print(mult(5,5))

points_2d = [(10, 2), (1, 15), (3, 20)]
p_sorted = sorted(points_2d, key=lambda x: x[1] - x[0])
print(p_sorted)

a = [1, 2, 3]

# map funct
b = map(lambda x: x*2, a)
print(list(b))

c = [x*2 for x in a]
print(c)

# filter funct
print(list(filter(lambda  x: x%2==0,a)))
c = [x for x in a if x%2 == 0]
print(c)

# reduce
print(reduce(lambda x,y: x*y, a))



