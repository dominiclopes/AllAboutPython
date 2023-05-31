#test_something.py
import pytest
import logging

foo = logging.getLogger('foo')
bar = logging.getLogger('bar')
baz = logging.getLogger('baz')

@pytest.yield_fixture(scope='session')
def session_thing():
    foo.debug('constructing session thing')
    yield
    foo.debug('destroying session thing')

@pytest.yield_fixture
def testcase_thing():
    foo.debug('constructing testcase thing')
    yield
    foo.debug('destroying testcase thing')

def test_one(session_thing, testcase_thing):
    foo.info('one executes')
    bar.warning('this test does nothing aside from logging')
    baz.info('extra log, rarely read')

def test_two(session_thing, testcase_thing):
    foo.info('two executes')
    bar.warning('neither does this')
    baz.info('extra log, not enabled by default')