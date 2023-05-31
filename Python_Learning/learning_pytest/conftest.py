import pytest


# Learning the use of fixture and yield_fixture
@pytest.yield_fixture(scope='session')
def first_session():
    print("Remember the walls I built")
    yield
    print("Baby they are tumbling down")


@pytest.yield_fixture(scope='session')
def second_session():
    print("Lets dance in style")
    yield
    print("Lets dance for a while")


@pytest.fixture(scope='session')
def third_session():
    print("To the left to the left")
    yield
    print("Everything you own to the left in the box")


# print("I'm in conftest.py")
#
#
# def pytest_runtest_setup(item):
#     # called for running each test in 'a' directory
#     print("setting up", item)
# #
# # def pytest_addoption(parser):
# #     print("Hey im doing my job pytest_addoption")
# #     # print(parser)
# #     # dominic_group = parser.getgroup("dominic")
# #     # dominic_group.addoption()
# #     # print(dominic_group)
# #     pass


# #conftest.py
# import os
#
# def pytest_logger_config(logger_config):
#     logger_config.add_loggers(['foo', 'bar', 'baz'], stdout_level='info')
#     logger_config.set_log_option_default('foo,bar')
#
# def pytest_logger_logdirlink(config):
#     return os.path.join(os.path.dirname(__file__), 'mylogs')