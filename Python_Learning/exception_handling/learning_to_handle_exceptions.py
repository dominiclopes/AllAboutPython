# try:
#     raise NameError("Hi there")  # Raise Error
# except NameError:
#     print("An exception")
#     raise  # To determine whether the exception was raised or not



try:
    a = 19/0
except ZeroDivisionError:
    raise
