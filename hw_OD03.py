
def bubble_sort(arr):
    """Пузырьковая сортировка (Bubble Sort)"""
    n = len(arr)
    for run in range(n-1):
        for i in range(n-1-run):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


def selection_sort(arr):
    """Сортировка выбором (Selection Sort)"""
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    """Сортировка вставками (Insertion Sort)"""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """Сортировка слиянием (Merge Sort)"""
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr):
    """Быстрая сортировка (Quick Sort)"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def heap_sort(arr):
    """Пирамидальная сортировка (Heap Sort)"""
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


def shell_sort(arr):
    """Сортировка Шелла (Shell Sort)"""
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


def counting_sort(arr):
    """Сортировка подсчетом (Counting Sort)"""
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m

    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr


def radix_sort(arr):
    """Поразрядная сортировка (Radix Sort)"""
    RADIX = 10
    placement = 1
    max_digit = max(arr)

    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        for i in arr:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                arr[a] = i
                a += 1
        placement *= RADIX
    return arr


def bucket_sort(arr):
    """Сортировка ведрами (Bucket Sort)"""
    bucket = []
    slot_num = 10
    for i in range(slot_num):
        bucket.append([])

    for j in arr:
        index_b = int(slot_num * j)
        bucket[index_b].append(j)

    for i in range(slot_num):
        bucket[i] = insertion_sort(bucket[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr


def print_menu():
    print("Алгоритмы сортировки")
    print("1. Пузырьковая сортировка")
    print("2. Сортировка выбором")
    print("3. Сортировка вставками")
    print("4. Сортировка слиянием")
    print("5. Быстрая сортировка")
    print("6. Пирамидальная сортировка")
    print("7. Сортировка Шелла")
    print("8. Сортировка подсчетом")
    print("9. Поразрядная сортировка")
    print("10. Сортировка ведрами")
    print("0. Выход")


def main():
    algorithms = {
        1: bubble_sort,
        2: selection_sort,
        3: insertion_sort,
        4: merge_sort,
        5: quick_sort,
        6: heap_sort,
        7: shell_sort,
        8: counting_sort,
        9: radix_sort,
        10: bucket_sort
    }

    descriptions = {
        1: "Пузырьковая сортировка — простой алгоритм, который многократно проходит по списку, сравнивая соседние элементы и меняя их местами, если они находятся в неправильном порядке.",
        2: "Сортировка выбором находит минимальный элемент и перемещает его в начало, затем повторяет процесс для оставшейся части списка.",
        3: "Сортировка вставками строит отсортированный список, по одному элементу добавляя его на нужное место.",
        4: "Сортировка слиянием рекурсивно делит список пополам, сортирует каждую половину, а затем сливает их в один отсортированный список.",
        5: "Быстрая сортировка выбирает опорный элемент и делит список на две части — элементы меньше опорного и больше, затем рекурсивно сортирует каждую часть.",
        6: "Пирамидальная сортировка строит двоичную кучу (heap) из списка и затем последовательно извлекает максимальный элемент.",
        7: "Сортировка Шелла улучшает сортировку вставками, сначала сортируя элементы, находящиеся на некотором расстоянии друг от друга.",
        8: "Сортировка подсчетом подсчитывает количество вхождений каждого элемента и использует эту информацию для сортировки.",
        9: "Поразрядная сортировка сортирует числа поразрядно, начиная с младшего разряда.",
        10: "Сортировка ведрами распределяет элементы по ведрам, сортирует каждый ведро и затем объединяет результат."
    }

    while True:
        print_menu()
        choice = int(input("Выберите алгоритм (0 для выхода): "))
        if choice == 0:
            break
        if choice in algorithms:
            arr = [int(x) for x in input("Введите элементы списка через пробел: ").split()]
            print(f"\n{descriptions[choice]}")
            sorted_arr = algorithms[choice](arr)
            print(f"Отсортированный список: {sorted_arr}\n")
        else:
            print("Неверный выбор. Пожалуйста, выберите заново.\n")


if __name__ == "__main__":
    main()
