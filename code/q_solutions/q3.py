# Given an array of strings, find the average string length

n = ['12313','123123123', 'fasdfasdfa', 'hippopotamus', '234234234', '1', '1']

def averageLength(n):
    result = 0

    for item in n:
        result += len(item)

    result = result / len(n)
    return result

print(averageLength(n))