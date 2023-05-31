import re
import time

a = [None, 1, 2 ,3, None, False, False, True, "<NULL>", True, 8, 129, 34, None, None, 764, "<NULL>", "<EMPTY>"]
replace_string_dict = {None:"None", True:"True", False: "False"}
# match_found = re.search(r"^<(?P<value>.*)>$", str(data).strip())
#             if match_found:
#                 data = "&lt;" + match_found.group('value') + "&gt;"

start = time.time()
for replace_string in replace_string_dict:
    try:
        while True:
            a[a.index(replace_string)] = replace_string_dict[replace_string]
    except ValueError:
        pass
print(a)
print("Time Taken by logic 1: {}".format(time.time()-start))
print("-" * 50)


a = [None, 1, 2 ,3, None, False, False, True, "<NULL>", True, 8, 129, 34, None, None, 764, "<NULL>", "<EMPTY>"]
start = time.time()
for n, i in enumerate(a):
    for replace_string in replace_string_dict:
        if i == replace_string:
            a[n] = replace_string_dict[replace_string]
print(a)
print("Time Taken by logic 2: {}".format(time.time()-start))
print("-" * 50)


a = [None, 1, 2 ,3, None, False, False, True, "<NULL>", True, 8, 129, 34, None, None, 764, "<NULL>", "<EMPTY>"]
start = time.time()
for replace_string in replace_string_dict:
    a = [replace_string_dict[replace_string] if x == replace_string else x for x in a]
print(a)
print("Time Taken by logic 3: {}".format(time.time()-start))
print("-" * 50)


# start = time.time()
# map(lambda x: x if x != 4 else 'sss', a)
# print("Time Taken by logic 4: {}",format(time.time()-start))
# print("-" * 50)


# Writing a lambda function that takes in regular expression and value and returns the output
a = [None, 1, 2 ,3, None, False, False, True, "<NULL>", True, 8, 129, 34, None, None, 764, "<NULL>", "<EMPTY>"]
replace_string_dict = {None:"None", True:"True", False: "False", r"^<(?P<value>.*)>$": "&lt;" + match_found.group('value') + "&gt;"}
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
regex = r"^<(?P<value>.*)>$"
m = lambda regex, data: "Solved" if re.search(regex, data) else data
