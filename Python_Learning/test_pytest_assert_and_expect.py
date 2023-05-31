from pytest_expect import expect

def test_1():
    assert 1 == 1
    assert 2 == 1
    assert 3 == 3


def test_2():
    expect(1 == 1)
    expect(2 == 1)
    expect(3 == 3)
