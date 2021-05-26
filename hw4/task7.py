from sys import argv

def fact(num):
    a = 1
    for i in range(1,num + 1):
        a *= i 
        yield a

for el in fact(int(argv[1])):
    print(el)