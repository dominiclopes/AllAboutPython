import timeit
from timeit import Timer

a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = [11,12,13,14,15,16,17,18]


def test1():
    pass


def test2():
    d = a + b + c


def test3():
    d = []
    d.extend(a)
    d.extend(b)
    d.extend(c)


def test4():
    d = [value for value in (value_list for value_list in [a,b,c])]


def test5():
    d = []
    for value_list in [a, b, c]:
        for value in value_list:
            d.append(value)


t = Timer("test1", "from __main__ import test1")
print("test1", t.timeit(number=100), "milliseconds")
t = Timer("test2", "from __main__ import test2")
print("test2", t.timeit(number=100), "milliseconds")
t = Timer("test3", "from __main__ import test3")
print("test3", t.timeit(number=100), "milliseconds")
t = Timer("test4", "from __main__ import test4")
print("test4", t.timeit(number=100), "milliseconds")
t = Timer("test5", "from __main__ import test5")
print("test5", t.timeit(number=100), "milliseconds")