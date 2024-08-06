def get_matrix(n, m, value):
    # Создаем пустой список для матрицы
    matrix = []

    # Проверяем, если n или m меньше или равно 0, возвращаем пустой список
    if n <= 0 or m <= 0:
        return matrix

    # Внешний цикл для создания строк матрицы
    for i in range(n):
        # Создаем пустую строку
        row = []

        # Внутренний цикл для заполнения строки значениями
        for j in range(m):
            row.append(value)

        # Добавляем строку в матрицу
        matrix.append(row)

    # Возвращаем заполненную матрицу
    return matrix


# Пример использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Выводим результаты на консоль
print(result1)
print(result2)
print(result3)