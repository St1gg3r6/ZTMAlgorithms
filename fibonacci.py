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
    


def fibonacci_recursive_cached():
    fib = {1: 1, 2: 1}
    def fib_inner(n):
        if n in fib:
            return fib[n]
        fib[n] = fib_inner(n - 1) + fib_inner(n - 2)
        return fib[n]
    return fib_inner

# print(fibonacci_iterative(5))
# print(fibonacci_recursive(5))
# print(fibonacci_recursive_cached(5))
fib_seq = fibonacci_recursive_cached()
print(fib_seq(100))
