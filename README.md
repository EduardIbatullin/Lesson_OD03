# Lesson_OD03. Алгоритмы сортировки.

---

# Алгоритмы сортировки на Python

## Описание проекта

Этот проект содержит реализацию десяти основных алгоритмов сортировки на языке Python. Программа предоставляет интерактивное меню, в котором пользователь может выбрать один из алгоритмов для сортировки заданного списка чисел. После выбора алгоритма на экран выводится краткое описание его работы и результат сортировки.

## Алгоритмы

В проекте реализованы следующие алгоритмы сортировки:

1. **Пузырьковая сортировка (Bubble Sort)**
2. **Сортировка выбором (Selection Sort)**
3. **Сортировка вставками (Insertion Sort)**
4. **Сортировка слиянием (Merge Sort)**
5. **Быстрая сортировка (Quick Sort)**
6. **Пирамидальная сортировка (Heap Sort)**
7. **Сортировка Шелла (Shell Sort)**
8. **Сортировка подсчетом (Counting Sort)**
9. **Поразрядная сортировка (Radix Sort)**
10. **Сортировка ведрами (Bucket Sort)**

## Использование

1. **Запуск программы**: Склонируйте репозиторий и запустите Python-скрипт:

    ```bash
    python hw_OD03.py
    ```

2. **Выбор алгоритма**: После запуска программы появится меню с номерами алгоритмов. Выберите нужный алгоритм, введя соответствующий номер.

3. **Ввод данных**: Введите список чисел, разделенных пробелами, который необходимо отсортировать.

4. **Получение результата**: Программа выполнит сортировку с использованием выбранного алгоритма и выведет на экран отсортированный список вместе с кратким описанием выбранного алгоритма.

### Пример работы программы

```bash
Алгоритмы сортировки
1. Пузырьковая сортировка
2. Сортировка выбором
3. Сортировка вставками
4. Сортировка слиянием
5. Быстрая сортировка
6. Пирамидальная сортировка
7. Сортировка Шелла
8. Сортировка подсчетом
9. Поразрядная сортировка
10. Сортировка ведрами
0. Выход
Выберите алгоритм (0 для выхода): 1
Введите элементы списка через пробел: 5 7 4 3 8 2

Пузырьковая сортировка — простой алгоритм, который многократно проходит по списку, сравнивая соседние элементы и меняя их местами, если они находятся в неправильном порядке.
Отсортированный список: [2, 3, 4, 5, 7, 8]
```

## Описание алгоритмов

### 1. Пузырьковая сортировка (Bubble Sort)
Алгоритм многократно проходит по списку, сравнивая соседние элементы и меняя их местами, если они находятся в неправильном порядке. Этот процесс повторяется до тех пор, пока список не будет отсортирован.

### 2. Сортировка выбором (Selection Sort)
Алгоритм находит минимальный элемент в неотсортированной части списка и меняет его местами с первым элементом этой части. Затем процесс повторяется для оставшейся неотсортированной части списка.

### 3. Сортировка вставками (Insertion Sort)
Алгоритм строит отсортированный список, добавляя по одному элементу и помещая его на нужное место по сравнению с уже отсортированными элементами.

### 4. Сортировка слиянием (Merge Sort)
Алгоритм рекурсивно делит список на две части, сортирует каждую из них, а затем объединяет (сливает) обратно в один отсортированный список.

### 5. Быстрая сортировка (Quick Sort)
Алгоритм выбирает опорный элемент и делит список на три части: элементы меньше опорного, равные ему и больше его. Затем рекурсивно сортирует левую и правую части.

### 6. Пирамидальная сортировка (Heap Sort)
Алгоритм строит двоичную кучу (heap) из списка и затем последовательно извлекает максимальный элемент, перестраивая кучу после каждого извлечения.

### 7. Сортировка Шелла (Shell Sort)
Алгоритм улучшает сортировку вставками, сначала сортируя элементы, находящиеся на некотором расстоянии друг от друга, затем постепенно уменьшая это расстояние.

### 8. Сортировка подсчетом (Counting Sort)
Алгоритм подсчитывает количество вхождений каждого элемента в список, а затем использует эту информацию для сортировки.

### 9. Поразрядная сортировка (Radix Sort)
Алгоритм сортирует числа по разрядам, начиная с младшего разряда и двигаясь к старшему.

### 10. Сортировка ведрами (Bucket Sort)
Алгоритм распределяет элементы по ведрам (группам), сортирует каждый ведро отдельно, а затем объединяет результаты в один отсортированный список.

## Требования

- Python 3.x

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности см. в файле `LICENSE`.

