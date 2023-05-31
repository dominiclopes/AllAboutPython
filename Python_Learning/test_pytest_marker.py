import pytest
from funcy import compose
# pytestmark = pytest.mark.abc
# pytestmark = pytest.mark.pqr

pytestmark = compose(pytest.mark.abc, pytest.mark.pqr)
print(pytestmark)

def test_1():
    print("Hello")


def test_2():
    print("Hello again")