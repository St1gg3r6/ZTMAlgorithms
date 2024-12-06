def find_factorial_recursive(number):

    if number <= 2:
        return number
    return number * find_factorial_recursive(number - 1)


def find_factorial_iterative(number):
    
    if number <= 2:
        return number
    result = 1
    for i in range(number):
        result *= i + 1
    return result


print(find_factorial_recursive(25))
print(find_factorial_iterative(25))
