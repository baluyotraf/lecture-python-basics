# Function Sample Code


# No return value
def function_1(x):
    x = 10


print(function_1(10))


# With return value
def function_2(x):
    return x


print(function_2(10))


# With default value
# With tuple return value
def function_3(w, x, y=10, z=20):
    return w, x, y, z


print(function_3(10, 20))
# Named Arguments
print(function_3(40, z=10, x=20, y=30))
# Argument Unpacking
print(function_3(*[10, 20], **{'y': 30, 'z': 40}))


# With args and kwargs
def function_4(*args, **kwargs):
    print('args:',  args)
    print('kwargs:', kwargs)


print(function_4(10, 20, a=30, b=40))