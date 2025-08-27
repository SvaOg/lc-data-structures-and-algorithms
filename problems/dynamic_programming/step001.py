memo = {}

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if not n in memo:
        print(f"Calculating fib({n})")
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]
    

print(fibonacci(7))
