import pytest


def test_1(first_session, second_session):
    print("Hi im test1")


def test_2(first_session, second_session):
    print("Hi im test2")


# @pytest.mark.usefixtures('')
# @pytest.mark.
def test_3(third_session):
    print("Hi im test3")

