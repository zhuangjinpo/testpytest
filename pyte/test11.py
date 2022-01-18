import pytest

@pytest.fixture(scope="module")
def login():
    print("login")

def test_1():
    print("test1")

def test_2():
    print("test2")

if __name__ == '__main__':
    pytest.main()