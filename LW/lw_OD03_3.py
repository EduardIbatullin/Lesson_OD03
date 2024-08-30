# Алгоритмы сортировки. Сортировка выбором (Selection Sort).

# Функция сортировки выбором.
def selection_sort(s):
    for i in range(len(s)):
        min_index = i
        for j in range(i + 1, len(s)):
            if s[j] < s[min_index]:
                min_index = j
        s[i], s[min_index] = s[min_index], s[i]
    return s


# Задаем список.
mas = [-3, 5, 0, -8, 1, 10]

# Выводим первоначальный список.
print(mas)

# Выводим отсортированный список.
print(selection_sort(mas))
