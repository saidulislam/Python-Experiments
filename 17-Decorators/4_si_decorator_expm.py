# 1
# typicall, you start with the following

# def say_hello():
#     user_name = input("Enter your name: ")
#     print(f"Hello {user_name}!")

# def welcome_user():
#     print(":: Welcome to my application ::")
#     say_hello()

# welcome_user()



# 2
# then you transition to something like the following
# higher order function
# you pass function as an argument to another function

# def say_hello():
#     user_name = input("Enter your name: ")
#     print(f"Hello {user_name}!")

# def welcome_user(func):
#     print(":: Welcome to my application ::")
#     func()

# # Calls both functions and prints both things.
# welcome_user(say_hello)


# 3
# very basic of a decorator

# def welcome_user(func):
#     print(":: Welcome to my application ::")
#     return func

# @welcome_user
# def say_hello():
#     user_name = input("Enter your name: ")
#     print(f"Hello {user_name}!")

# # Calls both functions and prints both things.
# say_hello()


# 4
# concept of wrapping a function
# import functools

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_function():
#         func()
#         print("Goodbye!")

#     return wrapper_function

# def say_hello():
#     print("Hello!")

# greet = decorator(say_hello)
# print(greet.__name__)  # without the functools wrap, it will say wrappper_function
# greet()  # Hello! and Goodbye!


# 5
# concept of wrapping a function
# and using the decorator
# import functools

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_function():
#         func()
#         print("Goodbye!")

#     return wrapper_function

# @decorator
# def say_hello():
#     print("Hello!")

# say_hello()



# 6
# decorating a function with parameters

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_function(*args, **kwargs):
        func(*args, **kwargs)
        print("Goodbye!")

    return wrapper_function

@decorator
def say_hello(name):
    print(f"Hello {name}!")

say_hello("Jake")

@decorator
def say_something_else(name, greeting="Hello"):
    print(f"{greeting} {name}!")

say_something_else(greeting="Howdy", name="Mark")