import cmath

class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt


class ComplexNumber:
    def __init__(self, real, img) -> None:
        self.real = real
        self.img = img
    @classmethod
    def split_comp(cls, data):
        data = str(data).split('+')
        data[0] = data[0].replace('(','')
        data[1] = data[1].replace('j)','')
        r, i = list(map(int, data))
        return cls(r, i)
    def __str__(self) -> str:
        return f'Number is {self.real} + i{self.img}'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)
    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.img * other.img, 
                            self.real * other.img + self.img * other.real)

    @staticmethod
    def check_corr(obj, n1, n2, type):
        if type == 'add':
            z3 = n1 + n2
        if type == 'mul':
            z3 = n1 * n2
        try:
            if int(z3.real) != obj.real:
                raise MyErr('Result is wrong!!')
            print(f'Result of {type} is correct')
        except MyErr as err:
            print(err)
            




num1 = 4 + 9j
num2 = 2 + 1j
my_num1 = ComplexNumber.split_comp(num1)
my_num2 = ComplexNumber.split_comp(num2)

res1 = my_num1 + my_num2
res2 = my_num1 * my_num2
print(res1)
print(res2)
ComplexNumber.check_corr(res1, num1, num2, 'add')
ComplexNumber.check_corr(res2, num1, num2, 'mul')
