# Функция сортировки пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Проход по всем элементам массива
        for j in range(0, n-i-1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Запрашиваем количество чисел
n = int(input("Введите количество чисел, которые хотите ввести: "))
numbers = []

# Запрашиваем n чисел у пользователя
for _ in range(n):
    num = float(input("Введите число: "))
    numbers.append(num)

# Сортируем числа
bubble_sort(numbers)

# Выводим отсортированный массив
print("Отсортированные числа:", numbers)
