import pytest

@pytest.mark.usefixtures("login")
def test_first():
    print("级别只运行一次1")

@pytest.mark.usefixtures("login")
def test_second():
    print("级别只运行一次2")

class TestCase():
    def test_1(self,login):
        '用例传fixture'
        print("测试账号：1")


    def test_2(self,login):
        '用例传fixture'
        print("测试账号：2")

if __name__ == '__main__':
    pytest.main(["-s","test06.py"])
