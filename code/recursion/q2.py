# Modify vertical suchg that it prints the numbers in reverse

n = 12345

def vertical(n):
    if n < 10:
        print(n)
    else:
        vertical(n//10)
        print(n%10)

def reverse(n):
    if n < 10:
        print(n)
    else:
        print(n%10)
        reverse(n//10)

vertical(n)
print()
reverse(n)