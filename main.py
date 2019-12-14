from random import randint
N = 3
M = 5


def outputMatrix(matrix):  # вывод матрицы на экран
    for row in matrix:
        for item in row:
            print('%.2d' % item, end=' ')
        print()

a = []
for i in range(N):  # заполнение строк матрицы случайными числами
    b = []
    for j in range(M):
        b.append(randint(1, 99))
    a.append(b)

print(a, end='\n\n')  # вывод двумерного массива

for i in range(N):  # сортировка внутри строки матрицы
    for j in range(M-1):
        for k in range(M - j - 1):
            if a[i][k] > a[i][k + 1]:
                a[i][k], a[i][k + 1] = a[i][k + 1], a[i][k]

outputMatrix(a)
print()

