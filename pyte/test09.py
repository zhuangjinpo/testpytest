import pytest



@pytest.mark.weibo
def test_1():
    print("in test_1")

@pytest.mark.weibo
def test_2():
    print("in test_2")

@pytest.mark.hongmi
def test_3():
    print("in test_3")

if __name__ == '__main__':
    pytest.main(["-v", "-s","-m","weibo","-n","3","test09.py"])

