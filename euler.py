
#Euler 1
def divby35(x):
    return x % 3 == 0 or x % 5 == 0

print(sum([x for x in range(1000) if divby35(x)]))

#Euler 2
