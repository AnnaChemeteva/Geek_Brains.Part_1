class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for el in self.matrix:
            print(el)

    def __add__(self, other):
        result = []
        number = []
        for el in range(len(self.matrix)):
            for i in range(len(self.matrix[0])):
                number.append(self.matrix[el][i] + other.matrix[el][i])
                if len(number) == len(self.matrix[0]):
                    result.append(number)
                    number = []
        return Matrix(result)


matrix_1 = Matrix([[1, 2], [3, 7], [5, 9]])
matrix_2 = Matrix([[5, 8], [2, 8], [1, 4]])

print(matrix_1.__str__())
print(matrix_1.__add__(matrix_2))
