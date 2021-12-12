import pytest


def test_1():
    print("tets_1")

def test_2():
    print("tets_2")

def test_3():
    print("tets_3")


if __name__ == '__main__':
    pytest.main("-v -s test06.py::test_1")