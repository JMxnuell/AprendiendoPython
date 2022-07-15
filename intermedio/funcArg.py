# func arg vs func param

# parameter:
def print_name(name):
    print(name)


# argument:
print_name('Manuel')


# positional and keyword arguments
def foo(a, b, c=9):  # default value
    print(a, b, c)


foo(a=2, b=3)


# variable lengths arguments
def foo2(a, b, *args, **kwargs):  # se pueden nombrar cómo sea
    print(a, b)
    for a in args:
        print(a)
    for key in kwargs:
        print(key, kwargs[key])


foo2(1, 2, 3, 4, 5, six=6, seven=7)


# force keyword arguments
def foo3(a, b, *, c, d):  # force the parameters to be keyword
    print(a, b, c, d)


foo3(1, 2, d=4, c=3)


# unpacking arguments:
def foo4(a, b, c):
    print(a, b, c)


maList = [1, 2, 3]
foo4(*maList)  # be careful with upperbound


# local vs global
def foo5():
    # global number  # the global keyword must be used to make use of a global variable
    number = 3
    x = number
    number = 4
    print('number inside function: ', x)


number = 0

foo5()
print(number)


# PARAMETER PASSING: (call by object reference)
def foo6(l):
    l.append(4)
    l[0] = -100


l = [1, 2, 3]
foo6(l)
print(l)

