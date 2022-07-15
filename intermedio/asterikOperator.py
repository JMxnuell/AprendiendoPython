# *
# multiplication operation
result = 5 * 8
print(result)


# pow operation
result = 2 ** 2
print(result)

# create tuples, lists or strings with repeated elements
zeros = [0, 1] * 10
print(zeros)


# args, kwargs, keywords only arguments: (functions arguments):
# def foo(a, b, *arg, **kwargs): # topic already seen

# argument unpacking
# maList = [0, 1, 2]
# foo(*maList) -> numbers of parameters must be match
# foo (**myDict) -> for dictionaries

# unpacking containers:
numbers = [1, 2, 3, 4, 5, 6]
*beginning, last = numbers
print(beginning, last)

A = [(1, 2, 3), (4, 5, 6)]                       # list A = 2 tuples of 3
print([*zip(*A)])

d1 = {'A': 'a', 'B': 'b'}
d2 = {'C': 'c', 'D': 'd'}
print({**d1, **d2})  # merge two dictionaries


