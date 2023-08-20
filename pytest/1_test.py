class Reverse:

    def __init__(self, data) -> None:
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


rev = Reverse("spam")

for char in rev:
    print(char)
    print()

'''
The for statement calles iter() on the object. the func returns an iterator object
which defines the method __next__() which accesses elements in the container once at a time.
When there are no more elements, __next__() raises a StopIteration exception which tells the 
for loop to terminate.
'''


# Generators

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse("gold"):
    print(char)
    print()


class MyClass:
    class_variable = 0

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    # using this decorator is important here to define it's a class methods
    def class_method(cls):
        print("This is a class method.")
        print("Accessing class variable:", cls.class_variable)


MyClass.class_method()
