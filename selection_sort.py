numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selection_sort(numbers):

    for i in range(len(numbers)):
        lowest = numbers[i]
        lowest_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < lowest:
                lowest = numbers[j]
                lowest_index = j
        if lowest != numbers[i]:
            temp = numbers[i]
            numbers[i] = numbers[lowest_index]
            numbers[lowest_index] = temp

    return numbers

numbers = selection_sort(numbers)
print(numbers)
