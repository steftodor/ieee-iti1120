# create a function that performs a recursive binary search

x = [1,2,3,4,5]
n = 9

def search(lst, target, i, j):
    mid = (i+j) // 2
    if lst[mid] == target:
        return mid
    elif target > lst[mid]:
        return search(lst, target, mid+1, j)
    else:
        if i == j:
            return -1
        else:
            return search(lst, target, i, mid)

print(search(x, n, 0, len(x)-1))