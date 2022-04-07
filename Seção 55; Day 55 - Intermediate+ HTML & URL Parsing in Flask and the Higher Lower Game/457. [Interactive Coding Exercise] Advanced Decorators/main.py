# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}\nIt returned {function(*args)}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(*args):
    sum_ = 0
    for arg in args:
        sum_ += arg
    return sum_


a_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
