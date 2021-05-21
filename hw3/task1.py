a = int(input('Enter a first number:'))
b = int(input('Enter a second number:'))

def dev(a,b) -> float:
    if b == 0:
        b = int(input('Second number is zero, devision forbidden. Please enter another number:'))
    return a/b

print('Result is %f' % dev(a, b))
