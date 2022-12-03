# Find the number of palindromes in a given array of strings
# How fast can you make this?


n = ['123', '1221', '12331', '1233321', '123123321321', '111', '1']

def palindromes(n):
    e = []

    for w in n:
        if w[::-1] == w:
            e.append(w)

    return len(e)

print(palindromes(n))