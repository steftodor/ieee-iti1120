import generatedLists

def func_cubic(values):
    # example of a cubic complexity function
    # the number of operations is proportional to the cube of
    # the number of items in the list
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
print("Sum: ", func_cubic(generatedLists.tenItemList))
print("List of 20 items")
print("Sum: ", func_cubic(generatedLists.twentyItemList))
print("List of 30 items")
print("Sum: ", func_cubic(generatedLists.thirtyItemList))
print("List of 40 items")
print("Sum: ", func_cubic(generatedLists.fortyItemList))
print("List of 50 items")
print("Sum: ", func_cubic(generatedLists.fiftyItemList))
print("List of 60 items")
print("Sum: ", func_cubic(generatedLists.sixtyItemList))
print("List of 70 items")
print("Sum: ", func_cubic(generatedLists.seventyItemList))
print("List of 80 items")
print("Sum: ", func_cubic(generatedLists.eightyItemList))
print("List of 90 items")
print("Sum: ", func_cubic(generatedLists.ninetyItemList))
print("List of 100 items")
print("Sum: ", func_cubic(generatedLists.hundredItemList))
print("List of 200 items")
print("Sum: ", func_cubic(generatedLists.twoHundredItemList))
print("List of 300 items")
print("Sum: ", func_cubic(generatedLists.threeHundredItemList))
print("List of 400 items")
print("Sum: ", func_cubic(generatedLists.fourHundredItemList))
print("List of 500 items")
print("Sum: ", func_cubic(generatedLists.fiveHundredItemList))
print("List of 600 items")
print("Sum: ", func_cubic(generatedLists.sixHundredItemList))
print("List of 700 items")
print("Sum: ", func_cubic(generatedLists.sevenHundredItemList))
print("List of 800 items")
print("Sum: ", func_cubic(generatedLists.eightHundredItemList))
print("List of 900 items")
print("Sum: ", func_cubic(generatedLists.nineHundredItemList))
print("List of 1000 items")
print("Sum: ", func_cubic(generatedLists.thousandItemList))