
#Euler 2

def fib(n):
    a = 1
    b = 2
    for i in range(n):
        print(a)
        temp = a + b
        a = b
        b = temp


def fib1(n):
    a = 1
    b = 2
    for i in range(n):
        yield a,
        print(a)
        a, b = b, a + b


print("hello")
