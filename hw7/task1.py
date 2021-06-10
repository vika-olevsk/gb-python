class Matrix:
    def __init__(self, mat):
        self.matrix = mat

    def __str__(self):
        full = ''
        for el in self.matrix:
            el = list(map(str, el))
            full += (' '.join(el))+'\n'
        return full

    def __add__(self, other):
        summ = []
        for i in range(len(self.matrix)): 
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            summ.append(row)
        return Matrix(summ)



m1 = Matrix([[1,2,0,1], [2,3,2,0], [4,5,0,0]])
print(m1)

m2 = Matrix([[1,2,5,3], [2,3,2,1], [4,5,9,8]])
print(m1 + m2)