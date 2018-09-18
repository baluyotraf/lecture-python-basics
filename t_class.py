# Classes Sample Code


class Parent:

    # Class Attributes
    a = 10

    # Constructor
    def __init__(self, x):
        # Instance Attributes
        self._x = x

    # Method
    def get_x(self):
        return self._x

    # Class Method
    @classmethod
    def get_a(cls):
        return cls.a


# Inheritance
class Child(Parent):

    def __init__(self, x, y):
        # Calling parent function
        super().__init__(x)
        self._y = y
