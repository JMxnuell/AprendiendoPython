# function that take other func
import functools
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

#print_name = start_end_decorator(print_name) -> se evita con el decorator

#print(help(add5))
print(add5.__name__)

def repeat(n):
    def dec_Rep(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = f(*args, **kwargs)
            return result
        return wrapper
    return dec_Rep

@repeat(3)
def greet(name):
    print(name)

greet('Manuel')
