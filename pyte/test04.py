import pyte


def setup_module():
    print("setup_module")


def teardown_module():
    print("teardown_module")


def setup_function():
    print("setup_function")


def teardowm_function():
    print("teardowm_function")


def test_1():
    print("test_1")

class TestDemo1(object):


    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardowm_class")

    def setup_method(self):
        print("setup_method")

    def teardowm_method(self):
        print("teardown_method")

    def test_class(self):
        print("test_class")

if __name__ == '__main__':
    pyte.main()


