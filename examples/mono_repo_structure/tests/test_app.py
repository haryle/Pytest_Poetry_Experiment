from src.service1.mypkg.app import fib


def test_one():
    assert fib(1) == 1


def test_zero():
    assert fib(0) == 0


def test_two():
    assert fib(2) == 1


def test_three():
    assert fib(3) == 2
