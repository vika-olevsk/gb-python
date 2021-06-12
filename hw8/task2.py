class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt


data = input('Enter two numbers for devision sep with space:')
a, b = list(map(int, data.split()))

try:
    if b == 0:
        raise MyErr('Can not devide by zero!!')
    print(a / b)
except MyErr as err:
    print(err)