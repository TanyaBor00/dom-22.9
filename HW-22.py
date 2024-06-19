def binary_search(array, any_number, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] >= any_number and array[middle - 1] < any_number:
        return middle - 1
    elif any_number < array[middle]:
        return binary_search(array, any_number, left, middle - 1)
    else:
        return binary_search(array, any_number, middle + 1, right)


array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
any_number = int(input("Ведите любое число: "))
print("Сортированный список", sorted(array))
left = float(array[0])
right = float(array[-1])
if any_number < left or any_number > right:
    print("Числа нет в списке")
else:
    print("Индекс элемента, ближайшего минимальному от введенного числа", binary_search(array, any_number, 0, len(array) - 1))
