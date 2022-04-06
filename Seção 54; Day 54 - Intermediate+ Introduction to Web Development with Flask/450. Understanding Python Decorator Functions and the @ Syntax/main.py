# Functions can have inputs/functionality/output
import time


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(multiply, 2, 3)
print(result)


# Nested Functions
def outer_function():
    print("I'm outer")

    # The scope of the inner function is only accessible inside the outer_function
    def nested_function():
        print("I'm inner")

    nested_function()


outer_function()


# Functions can be returned from other functions
def outer_function2():
    print("I'm outer2")

    def nested_function2():
        print("I'm inner2")

    return nested_function2


inner_function = outer_function2()
inner_function()  # Caso essa linha estivesse comentada, só seria printado o valor "I'm outer2" e a função
# nested_function seria atribuída à variável inner_function.


# Python Decorator Function: Decorators are functions that wrap another functions to give them  additional functionality
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


def say_bye():
    print("Bye")


@delay_decorator
def say_greeting():
    print("How are you?")


# Triggering the method by its own name, but with added functionality from other function because of the @ sign
say_hello()  # 2 times with delay
say_bye()  # 1 time with no delay
say_greeting()  # 2 times with delay

# +/- the same thing of doing:
decorated_function = delay_decorator(say_bye)
decorated_function()
