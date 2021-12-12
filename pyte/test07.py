import pytest


@pytest.mark.flaky(reruns=3, reruns_delay=1)
def test_1():
    print("test_1")
    assert 1 == 1

def setup_module():
    print("in setup_module")

def teardown_module():
    print("in teardown_module")

def setup_function():
    print("in setup_function")

def teardown_function():
    print("in teardown_function")

# def test_2():
#     print("test_2")
#     pytest.assume(2==2)
#     pytest.assume(2 == 2)

def test_3():
    print("test_3")

class Testcase1():

    def setup_class(self):
        print("in setup_class")

    def teardown_class(self):
        print("in teardown_class")

    def setup_method(self):
        print("in setup_method")

    def teardown_method(self):
        print("in teardown_method")


    def test_c1(self):
        print("in class 1")

    def test_c2(self):
        print("in class 2")

    def test_c3(self):
        print("in class 3")

if __name__ == '__main__':
    pytest.main(["-v","-s", "test07.py"])

