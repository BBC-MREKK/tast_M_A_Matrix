def solve(n, m):
    # Создайте матрицу M размера n x m
    matrix = [[0] * m for _ in range(n)]

    # Заполните первую строку матрицы M перестановкой длины m
    matrix[0] = list(range(1, m + 1))

    # Заполните остальные строки сдвигом первой строки
    for i in range(1, n):
        matrix[i] = matrix[i - 1][1:] + [matrix[i - 1][0]]

    return matrix

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = solve(n, m)
    # Выведите максимальное значение s
    print(m)
    # Выведите матрицу M
    for row in result:
        print(" ".join(map(str, row)))