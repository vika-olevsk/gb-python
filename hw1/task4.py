n = int(input('Enter number:'))

Largest = 0
while n:
    r = n % 10
    if Largest < r:
        Largest = r
    n = int(n/10)
print('Largest digit is %d' % Largest)
# just comment