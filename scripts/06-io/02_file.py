# Sample Code for file IO


# Writing a text file
with open('file.txt', 'w') as file:
    file.write('content')

# Reading a text file
with open('file.txt', 'r') as file: # 'r' is optional argument
    print(file.read())


# Writing a binary file
with open('file.blob', 'wb') as file:
    file.write(bytes([0, 128, 255]))

# Reading a binary file
with open('file.blob', 'rb') as file: # 'r' is optional argument
    print(file.read())
