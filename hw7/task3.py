class Cell:
    def __init__(self, n):
        self.num = int(n)

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num > other.num:
            return Cell(self.num - other.num)
        else:
            print('Can not subtract, the second cell is bigger than the first one')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num / other.num)

    def __str__(self):
        return f'{self.num}'

    def make_order(self, k):
        line = ''
        i = 0
        while i < self.num:
            if i > 0 and i % k == 0:
                line += '\n'
            line += '*'
            i += 1
        print(line)



cell1 = Cell(14)
cell2 = Cell(70)
cell3 = Cell(10)

print(cell1 + cell2 + cell3)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)

cell1.make_order(5)


