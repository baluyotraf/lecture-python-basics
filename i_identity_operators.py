# Identity Operators Sample Code

integer1 = 10
integer2 = 10
class_instance1 = tuple('value')
class_instance2 = tuple('value')

# Identity
print(integer1 is integer2)
print(class_instance1 is class_instance2)

# Non-identity
print(integer1 is not integer2)
print(class_instance1 is not class_instance2)