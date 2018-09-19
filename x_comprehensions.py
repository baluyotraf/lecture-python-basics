# Sample Code for Comprehension Expressions

base_list = [0, 1, 2, 3, 4, 5]

# Traditional List Operation
trad_list = []
for i in base_list:
    if i % 2 == 0:
        i2 = i * 2
        trad_list.append(i2)

# List Comprehension
comp_list = [i * 2 for i in base_list if i % 2 == 0]
print(trad_list, comp_list)

# Traditional Set Operation
trad_set = set()
for i in base_list:
    if i % 2 == 0:
        i2 = i * 2
        trad_set.add(i2)

# Set Comprehension
comp_set = {i * 2 for i in base_list if i % 2 == 0}
print(trad_set, comp_set)

# Traditional Dictionary Operation
trad_dict = {}
for i in base_list:
    if i % 2 == 0:
        i2 = i * 2
        trad_dict[i] = i2

# Dictionary Comprehension
comp_dict = {i: i*2 for i in base_list if i % 2 == 0}
print(trad_dict, comp_dict)

