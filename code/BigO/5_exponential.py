import generatedLists

def func_exponential(values):
    # example of an exponential complexity function
    # the number of operations is proportional to 2^n
    # where n is the number of items in the list
    sum = 0
    opp_counter = 0
    for val in values:
        for val2 in values:
            for val3 in values:
                sum = sum + val + val2 + val3
                opp_counter += 1 # to help us understand the complexity
    print('Number of operations: ', opp_counter)
    return sum

print("List of 10 items")
print("Sum: ", func_exponential(generatedLists.tenItemList))
print("List of 20 items")
print("Sum: ", func_exponential(generatedLists.twentyItemList))
print("List of 30 items")
print("Sum: ", func_exponential(generatedLists.thirtyItemList))
print("List of 40 items")
print("Sum: ", func_exponential(generatedLists.fortyItemList))
print("List of 50 items")
print("Sum: ", func_exponential(generatedLists.fiftyItemList))
print("List of 60 items")
print("Sum: ", func_exponential(generatedLists.sixtyItemList))
print("List of 70 items")
print("Sum: ", func_exponential(generatedLists.seventyItemList))
print("List of 80 items")
print("Sum: ", func_exponential(generatedLists.eightyItemList))
print("List of 90 items")
print("Sum: ", func_exponential(generatedLists.ninetyItemList))
print("List of 100 items")
print("Sum: ", func_exponential(generatedLists.hundredItemList))