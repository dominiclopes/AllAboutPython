# # find first non-repeating character of the str
# str1 = "manmade"
#
#
# for c in str1:
#
#     if len([v for v in str1 if c == v]) == 1:
#         print(c)
#         break
#
#     # print(index, c, str1[index:], temp)

# ----------------------------------------
# # remove the second-largest element from the list
# lst1 = [1, 6, 4, 5, 9, 8, 7]
#
# # sort the list
# for i in range(len(lst1)):
#     for j in range(i, len(lst1)):
#         # print(lst1[i], lst1[j])
#         if lst1[i] > lst1[j]:
#             lst1[i], lst1[j] = lst1[j], lst1[i]
#     print(lst1)
# second_largest_element = lst1[-2]
# print(f"Second largest element in {lst1} is {second_largest_element}")
# lst1.remove(second_largest_element)
# print(f"List after removing the second largest element is {lst1}")
#
# ----------------------------------------
# # use decorator to find the execution time of a function
# import time
#
#
# def time_taken(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Time taken {end_time-start_time} seconds")
#     return wrapper
#
#
# @time_taken
# def sum_of_numbers(a, b):
#     print(a+b)
#
# sum_of_numbers(5, 6)

# ----------------------------------------
# copy 2 dictionaries to one
# dict3 = {**dict1, **dict2}


# ----------------------------------------
