# Lambda Expressions Sample Code


# Prints a function
def print_function(f):
    print(f)


# Can't declare a function without name
def sample_function_1(x):
    return x * 2


print_function(sample_function_1)
# Declare the sample_function_1 using lambda
sample_function_2 = lambda x: x * 2

# Verify that they are the same
print(sample_function_1(10))
print(sample_function_2(10))

# Rather than assigning lambda expression
# We can directly use it as function argument
# In this case, the name is not needed
print_function(lambda x: x*2)

