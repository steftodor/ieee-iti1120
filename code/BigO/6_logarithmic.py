def func_logarithmic(n):
    # example of a logarithmic complexity function
    # the number of operations is proportional to the logarithm of
    # the input

    # number of times we can divide n by 2 before we get 1
    c = 0
    op_counter = 0
    while n > 1:
        n = n / 2
        c += 1
        op_counter += 1 # to help us understand the complexity
    print('Number of operations: ', op_counter)
    return c


list = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]
for i in list:
    print("List of ", i, " items")
    print("Result: ", func_logarithmic(i))

 