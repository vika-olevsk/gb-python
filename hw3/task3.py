a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))

def my_func(a,b,c):
    list = [a,b,c]
    list.sort(reverse=True)
    return list[0]+list[1]

print(my_func(a,b,c))