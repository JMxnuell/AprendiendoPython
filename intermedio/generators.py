
# "yield instead of the return keyword
# "Cómo yo entiendo, yield almacena valores por cada iteración dentro de la función
def generator():
    yield 1
    yield 2
    yield 3

g = generator()
#print(g)

'''
value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)
'''

#print(sum(g))

#print(sorted(g))

def Countdown(n):
    print('s')
    while n > 0:
        yield str(n)
        n -= 1

print(' '.join(Countdown(4)))

# save memory when you work with large data

# yield evita usar memoria para este tipo de cosas:
def fn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num +=1
    return nums

l = fn(10)
print(sum(l))

def fn(n):
    num = 0
    while num < n:
        yield  num
        num +=1

print(sum(fn(10)))

# Fibonacci sequence with yield
def fibo(n):
    # 0 1 1 2 3 5 8
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

for i in fibo(10):
    print(i)

mygene = (i for i in range(10) if i % 2 == 0)
for i in mygene:
    print(i)
