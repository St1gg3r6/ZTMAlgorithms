def fibonacci_iterative(n):
    a = 0
    b = 0
    for i in range(1, n):
        if i == 1:
            a = 0
            b = 1
            result = 1
        result = a + b
        a = b
        b = result
    return result


def fibonacci_recursive(n):    
    if n <= 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    

fib = {1: 1, 2: 1}
def fibonacci_recursive_cached(n):
    if n in fib:
        return fib[n]
    fib[n] = fibonacci_recursive_cached(n - 1) + fibonacci_recursive_cached(n - 2)
    return fib[n]

# print(fibonacci_iterative(5))
# print(fibonacci_recursive(5))
print(fibonacci_recursive_cached(5))
