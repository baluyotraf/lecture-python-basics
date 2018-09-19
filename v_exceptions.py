# Sample Code for Exceptions

# Catch single exception
x = 'hello'
try:
    int(x)
except ValueError:
    print('Cannot convert', x)


# Catch multiple exception
y = [1, 2, 3]
try:
    float(y)
except (ValueError, TypeError):
    print('Cannot convert', y)

# Catch exception and use it
z = 'world'
try:
    float(z)
except ValueError as e:
    print('Error with message:', e)
