def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Сравнение для сортировки по возрастанию или убыванию
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Запрос количества чисел у пользователя
n = int(input("Введите количество чисел для сортировки: "))
numbers = []

# Запрос чисел у пользователя
for _ in range(n):
    num = float(input("Введите число: "))
    numbers.append(num)

# Запрос порядка сортировки
order = input("Введите 'a' для сортировки по возрастанию или 'd' для сортировки по убыванию: ").strip().lower()

# Определение порядка сортировки
ascending = True if order == 'a' else False

# Сортируем массив
bubble_sort(numbers, ascending)

# Вывод отсортированного массива
print("Отсортированные числа:", numbers)
