# Given an array n, return the numbers with an even amount of digits in a list
# Can't convert these into strings

n = [1,2,3,4,5,66,7,55,133,55,1333,5,591919,12938,9123889,91928381]

def even(n):
    e = []

    for w in n:
        new_w = w
        t = 0
        while new_w != 0:
            new_w = new_w // 10
            t += 1
        if new_w < 1 and t % 2 == 0:
            e.append(w)
    return e

print(even(n))