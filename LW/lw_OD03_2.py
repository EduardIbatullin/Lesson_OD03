# Алгоритмы сортировки. Быстрая сортировка (Quick Sort).


# Функция быстрой сортировки.
def quick_sort(s):
    if len(s) <= 1:
        return s

    element = s[0]

    left = list(filter(lambda x: x < element, s))
    middle = [x for x in s if x == element]
    right = list(filter(lambda x: x > element, s))

    return quick_sort(left) + middle + quick_sort(right)


# Задаем список.
mas = [5, 2, 9, 0, 1, 5, 3]

# Выводим первоначальный список.
print(mas)

# Выводим отсортированный список.
print(quick_sort(mas))
