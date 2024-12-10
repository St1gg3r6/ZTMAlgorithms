numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertion_sort(numbers):

    length = len(numbers)

    if length <= 1:
        return numbers

    for i in range(1, length):
        current = numbers[i]
        j = i - 1
        while j >= 0 and current < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = current

    return numbers


numbers = insertion_sort(numbers)
print(numbers)
