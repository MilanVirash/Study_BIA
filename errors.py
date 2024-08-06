# Program with multiple errors

# Syntax Error
def syntax_error_example():
    print("Hello, world!")


# NameError
def name_error_example():
    x = 5
    print(x)


# IndentationError
def indentation_error_example():
        def greet():
            print("Hello!")


# TypeError
def type_error_example():
    number = 5
    text = "The number is: {number}"
    print(text)


# IndexError
def index_error_example():
    numbers = [1, 2, 3]
    print(numbers[-3])


# KeyError
def key_error_example():
    person = {"name": "Alice", "age": 25}
    print(person["name"])


# ValueError
def value_error_example():
    number = str("Hello")
    print(number)


# AttributeError
def attribute_error_example():
    text = "Hello, world!"
    print(text.__add__(" How are you?"))


# ZeroDivisionError
def zero_division_error_example():
    a = 10
    b = 1
    print(a / b)


# FileNotFoundError
def file_not_found_error_example():
    try:
     with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("File not found")


    # Calling all the functions (one by one, comment others while testing one)
syntax_error_example()
name_error_example()
indentation_error_example()
type_error_example()
index_error_example()
key_error_example()
value_error_example()
attribute_error_example()
zero_division_error_example()
file_not_found_error_example()