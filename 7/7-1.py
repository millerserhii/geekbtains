
class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        result = ""
        for i in self.matrix_list:
            for j in i:
                result += f"\t{j}"
            result += f"\n"
        return result

    def __add__(self, other):
        final_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[0])):
                final_list[i][j] = self.matrix_list[i][j] + other.matrix_list[i][j]
        return Matrix(final_list)


m1 = Matrix([[1, 2, 8], [4, 33, 6], [9, 45, 9]])
m2 = Matrix([[22, 8, 7], [6, 5, 4], [0, 2, 6]])
print(m1)
print(m2)
print(m1 + m2)
