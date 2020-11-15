from django.test import TestCase

# Create your tests here.

def f():
    raise SystemExit(1)


def test_mytest():
    with TestCase.raises(SystemExit):
        f()