# use of if-elif-else
# if True:
#     print("Hola from if !")
# else:
#     print("Hola from else!")
#
# ----------------------------------------------
# use of try-except-else-finally
# try:
#     a = 1/1
# except (ZeroDivisionError, FloatingPointError):
#     print("Hola from exception")
# else:
#     print("Hola from else!")
# finally:
#     print("Hola from finally!")
# ----------------------------------------------
# use of for-else
# for i in range(2, 10, 2):
#     if i == 6:
#         pass
#     print(i)
#
# else:
#     print("Hola from else!")
# ----------------------------------------------
# use of namedtuples
# from collections import namedtuple
#
# point = namedtuple("Point", "x y", defaults=[0, 0])
# a = point(1,2)
# b= point()
# print(a.x, a.y, type(a), type(point))
# print(b)
# ----------------------------------------------
# use of array
# import array
#
# a = array.array("i", [1,2,3,4])
# print(a[1])
# ----------------------------------------------
# use of enumerate
# for key, value in enumerate(["a", "w", "2"], start=1):
#     print(f"{key} --> {value}")
# # ----------------------------------------------
# # use of zip
# for a, b in zip([1,2,3], ['a', "b", "c", "d"]):
#     print(f"{a} --> {b}")
# # ----------------------------------------------
# # use of *args and **kwargs
# def sum(*args):
#     s = 0
#     for arg in args:
#         s += arg
#     print(f"Sum of {args} is {s}")
# sum(1,2,3,5)
# # ----------------------------------------------
# # # use of lambda functions
# square_or_cube = lambda x: x ** 2 if x % 2 == 0 else x ** 3
# print(square_or_cube(11))
# # ----------------------------------------------
# # use of iterators
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a *= 5
#
#         if x > 26:
#             raise StopIteration
#         return x
#
# n = iter(MyNumbers())
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# # ----------------------------------------------
# # # use of generator
import time
# def timeTaken(func):
#     start = time.time()
#     func()
#     total_time_taken = (time.time() - start)*60
#     print(f"Total time take by {func.__name__} is {total_time_taken}")
#
# def suma():
#     s = sum((v for v in range(10)))
#     time.sleep(5)
#     print(s)
#
# timeTaken(suma)
# # ----------------------------------------------
# # # use of decorator
# import functools
#
#
# def do_twice(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def repeat(num_of_times: int = 2):
#     def decorator_function(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             value = None
#             for _ in range(num_of_times):
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper
#     return decorator_function
#
#
# @repeat()
# # @do_twice
# def say_hi(name: str) -> str:
#     print(f"Hi {name}")
#     return f"{name} enjoy you day"

#
# print(say_hi("Bob"))
# # print(say_hi)
# # print(help(say_hi))
# # ----------------------------------------------
# # single ton class
# import time
# class SingleTon:
#     NO_OF_INSTANCE = 0
#
#     def __init__(self):
#         if SingleTon.NO_OF_INSTANCE == 1:
#             raise Exception("cannot create another object. SingleTon class")
#         SingleTon.NO_OF_INSTANCE += 1
#         print("Created SingleTon class object")
#
# s1 = SingleTon()
# time.sleep(2)
# s2 = SingleTon()
# # ----------------------------------------------
# # closures -> use of variables outside their scope
# def outer_function(text):
#     text += ", You all right?"
#
#     def inner_function():
#         print(text)
#
#     return inner_function
#
# outer_function("Bob")()
# # ----------------------------------------------
# classes and objects
# getter and setter
# class A:
#     def __init__(self):
#         self._a = 0
#
#     @property
#     def a(self):
#         print("Getter method")
#         return self._a
#
#     @a.setter
#     def a(self, value):
#         print("Setter method")
#         self._a = value
#
#     def info(self):
#         print(f"This is class {A.__name__}")
#
# class B():
#     def info(self):
#         print(f"This is class {B.__name__}")
#
# class C(A, B):
#     pass
#
# a_obj = A()
# print(a_obj.a)
# a_obj.a = 10
# print(a_obj.a)
# a_obj.info()
#
# b_obj = B()
# b_obj.info()
#
# c_obj = C()
# c_obj.info()
# # ----------------------------------------------
# # enum
# from enum import Enum
#
# class Status(Enum):
#     SUCCESS = 0
#     FAIL = 1
#     RETRIED = 2
#
# print(Status.SUCCESS.value, Status.SUCCESS.name, Status(0))
# # ----------------------------------------------
# example
# a = [1, 3, 4, 5, 2]
# b = [1, 2, 3, 6]
# if len(a) >= len(b):
#     status = all(True if value in a else False for value in b)
# else:
#     status = all([True if value in b else False for value in a])
# print(status)
# # ----------------------------------------------
# # file handling
# with open("temp.txt", "w") as file_obj:
#     file_obj.write("This is a temporary file")
# with open("temp.txt") as file_obj:
#     print(file_obj.read())
# # ----------------------------------------------
# import requests
#
# session = requests.Session()
#
# url = "https://reqres.in/api/users"
# response = session.get(url, params={"page": 2})
# print(f"response -> {response}")
# print(f"response url -> {response.url}")
# print(f"status code -> {response.status_code}")
# print(f"response in json -> {response.json()}")
# print(f"response headers -> {response.headers}")
# # ----------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
#
# driver_path = ChromeDriverManager().install()
# print(driver_path)
# driver = webdriver.Chrome(service=Service(driver_path))
# print(driver)
# # ----------------------------------------------
# recursive function python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(20):
    print(fibonacci(i))

