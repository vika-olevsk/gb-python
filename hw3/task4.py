x = float(input('Enter any positive number:'))
y = int(input('Enter an integer negative number:'))

# check that 2d number is negative
if y>0:
    y = -y

def func1(x,y):
    ''' ** approach '''
    print(f'Approach with ** gives {x**y}')

def func2(x,y):
    ''' Loop approach'''
    i = 1
    res = x
    while i < abs(y):
        res *= x
        i += 1
    print(f'Approach with loops gives {1/res}')

func1(x,y)
func2(x,y)