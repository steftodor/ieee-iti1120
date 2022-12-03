
def func_constant(values):
    # example of a constant complexity function
    # the number of operations is always the same
    # regardless of the number of items in the list
    temp = values[0] 
    var = temp * 20  
    ret = var / 3 
    return ret 

list = [1,2,3,4,5,6,7,8,9,10]
print(func_constant(list))

