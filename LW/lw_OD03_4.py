# Алгоритмы сортировки. Сортировка вставками (Insertion Sort).


# Функция сортировки вставками.
def insertion_sort(s):
    for i in range(1, len(s)):
        key = s[i]
        j = i - 1
        while j >= 0 and s[j] > key:
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = key
    return s


# Задаем список.
mas = [-3, 5, 0, -8, 1, 10]

# Выводим первоначальный список.
print(mas)

# Выводим отсортированный список.
print(insertion_sort(mas))
