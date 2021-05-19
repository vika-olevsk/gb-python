a = int(input('Enter first day result:'))
b = int(input('Enter needed result:'))

d = 1
while a < b:
    a *= 1.1 
    d += 1
print ('On the %d-th day you will achive the result, not less than %d km' % (d,b))