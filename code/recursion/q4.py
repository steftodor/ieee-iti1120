# find the facatorial of a number n; n>0 using the two methods

def loop_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial


def recursive_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n-1)


print(loop_factorial(5))
print(recursive_factorial(5))