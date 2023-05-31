class A(object):
    def __init__(self, number):
        print("parent", number)


class B(A):
    def __init__(self):
        super().__init__(5)


b = B()
