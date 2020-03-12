
    # my_lambdata/my_mod.py


### Enlarge

def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100


### Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
