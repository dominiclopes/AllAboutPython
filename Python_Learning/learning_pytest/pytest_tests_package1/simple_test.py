import logging

def inc(x):
    return x + 1


def test_answer1():
    logging.info("Im executing the test test_answer1")
    assert inc(3) == 4


def test_answer2():
    logging.info("Im executing the test test_answer2")
    assert inc(3) == 4