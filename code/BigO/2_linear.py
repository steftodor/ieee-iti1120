import generatedLists

def func_linear(values):
    # example of a linear complexity function
    # the number of operations is directly proportional
    # to the number of items in the list
    sum = 0
    opp_counter = 0
    for val in values: 
        sum = sum + val
        opp_counter += 1 # to help us understand the complexity
    print('Number of operations: ', opp_counter)
    return sum

print("List of 10 items")
print("Sum: ", func_linear(generatedLists.tenItemList))
print("List of 100 items")
print("Sum: ", func_linear(generatedLists.hundredItemList))
print("List of 1000 items")
print("Sum: ", func_linear(generatedLists.thousandItemList))
print("List of 10000 items")
print("Sum: ", func_linear(generatedLists.tenThousandItemList))
