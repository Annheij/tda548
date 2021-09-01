# package samples

#
# This is methods having lists or class objects as parameters and/or return types
#
def methods_list_obj_program():
    # Methods with lists ----------------------
    my_list = [1, 4, 7, 3, 9, 2]
    print(max_in(my_list) == 9)     # Method calls to max(), argument is my_list
    my_list = get_list_with(3, 5)
    print(my_list == [5, 5, 5])

    # Methods with class objects ------------------
    d = get_dog()
    print_dog(d)


# ----- Method declarations  ------------
# Class declaration with int return type and array param
def max_in(some_list):  # Find biggest value in array
    m = some_list[0]
    for item in some_list:
        if item > m:
            m = item
        return m


# Get a list with some size initialized with some value
# List return type!
def get_list_with(size, n):
    local_list = [n] * size  # Create list
    return local_list


# Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Class object as parameter (a dog object)
def print_dog(dog):
    print(f"My dog {dog.name} is now {dog.age} years old")


# object as return value
def get_dog():
    name = input("What's the name of the dog? >")
    years = int(input("How old is the dog? >"))
    d = Dog(name, years)
    d.age += 1  # Dog gets older, manipulation of object attribute
    return d  # Return the dog object


if __name__ == "__main__":
    methods_list_obj_program()
