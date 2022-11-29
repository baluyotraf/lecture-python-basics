# For Loop Sample Code

# Counting
for i in range(3):
    print(i)

# List/Tuple/Set
for i in ['a', 'b', 'c']:
    print(i)

# Dictionary Keys
for i in {'a': 1, 'b': 2}:
    print(i)

# Dictionary Values
for i in {'a': 1, 'b': 2}.values():
    print(i)

# Dictionary Key and Value
for k, v in {'a': 1, 'b': 2}.items():
    print(k, v)

# With Index
for idx, i in enumerate(['a', 'b', 'c']):
    print(idx, i)