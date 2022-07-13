
# Errors and exceptions

x = -5
# if x<10:
    # raise Exception('x shloud be positive') # genera excepción

# assert(x >= 0), 'x is not positive'

try:
    a = 5/1
    a += 10
except Exception as e: # catch the exception
    print("e: ")
    print(e)
else:
    print('everyting is fine')
finally:
    print('cleaning up..')

class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 10:
        raise ValueTooHighError('value is too high')

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
