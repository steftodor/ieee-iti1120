# print all the numbers from 0 to n (inclusive using the two common methods

def loop_print(n):
    for i in range(n+1):
        print(i)

def recursive_print(n):
    if n == 0:
        print(n)
    else:
        recursive_print(n-1)
        print(n)

recursive_print(10)
