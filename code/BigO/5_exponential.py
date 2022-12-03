import generatedLists
# define a global variable to count the number of operations
op_counter = 0




def func_exponential(v):
    global op_counter # to help us understand the complexity
    # example of an exponential complexity function
    # the number of operations is proportional to 2^n
    if v <= 1:
        return v
    op_counter += 1 # to help us understand the complexity

    return func_exponential(v-1) + func_exponential(v-2)
   

print("Get the 10th fibonacci number")
print(func_exponential(10))
print("Number of operations: ", op_counter)
op_counter = 0
print("Get the 20th fibonacci number")
print(func_exponential(20))
print("Number of operations: ", op_counter)
op_counter = 0
print("Get the 30th fibonacci number")
print(func_exponential(30))
print("Number of operations: ", op_counter)
op_counter = 0
print("Get the 40th fibonacci number")
print(func_exponential(40))
print("Number of operations: ", op_counter)
op_counter = 0
print("Get the 50th fibonacci number")
print(func_exponential(50))
print("Number of operations: ", op_counter)
op_counter = 0
print("Get the 60th fibonacci number")
print(func_exponential(60))
print("Number of operations: ", op_counter)
op_counter = 0
print("Get the 70th fibonacci number")
print(func_exponential(70))
print("Number of operations: ", op_counter)
op_counter = 0
print("Get the 80th fibonacci number")
print(func_exponential(80))
print("Number of operations: ", op_counter)
op_counter = 0
print("Get the 90th fibonacci number")
print(func_exponential(90))
print("Number of operations: ", op_counter)
op_counter = 0
print("Get the 100th fibonacci number")
print(func_exponential(100))
print("Number of operations: ", op_counter)
op_counter = 0

