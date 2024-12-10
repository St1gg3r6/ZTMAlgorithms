numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubble_sort(numbers):

    length = len(numbers) - 1

    while length > 0:
        for i in range(length):
            if numbers[i] > numbers[i + 1]:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
        length -= 1

    return numbers

numbers = bubble_sort(numbers)
print(numbers)
