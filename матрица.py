class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def transpose(self):
        """Транспонирование матрицы"""
        transposed = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(transposed)

    def frobenius_norm(self):
        """Норма Фробениуса (корень из суммы квадратов всех элементов)"""
        total = 0
        for i in range(self.rows):
            for j in range(self.cols):
                total += self.data[i][j] ** 2
        return total ** 0.5

    def first_norm(self):
        """Первая норма (максимум суммы по столбцам)"""
        max_sum = 0
        for j in range(self.cols):
            col_sum = 0
            for i in range(self.rows):
                col_sum += abs(self.data[i][j])
            if col_sum > max_sum:
                max_sum = col_sum
        return max_sum

    def infinity_norm(self):
        """Бесконечная норма (максимум суммы по строкам)"""
        max_sum = 0
        for i in range(self.rows):
            row_sum = sum(abs(self.data[i][j]) for j in range(self.cols))
            if row_sum > max_sum:
                max_sum = row_sum
        return max_sum

    def multiply_columns(self, other):
        """Умножение матриц по столбцам (позлементно)"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера")

        result = [[self.data[i][j] * other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def display(self, name="Матрица"):
        """Вывод матрицы"""
        print(f"{name}:")
        for row in self.data:
            print([round(x, 2) if isinstance(x, float) else x for x in row])
        print()

# Создание двух матриц
matrix1 = Matrix([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

matrix2 = Matrix([[9, 8, 7],
                  [6, 5, 4],
                  [3, 2, 1]])

# Вывод исходной матрицы
matrix1.display("Исходная матрица")

# Транспонирование и вывод
transposed = matrix1.transpose()
transposed.display("Транспонированная матрица")

# Вывод трёх норм для исходной матрицы
print("Три нормы исходной матрицы:")
print(f"Норма Фробениуса: {matrix1.frobenius_norm():.4f}")
print(f"Первая норма: {matrix1.first_norm():.4f}")
print(f"Бесконечная норма: {matrix1.infinity_norm():.4f}")
print()

# Умножение матриц по столбцам
result_matrix = matrix1.multiply_columns(matrix2)
result_matrix.display("Переумноженная матрица по столбцам")
