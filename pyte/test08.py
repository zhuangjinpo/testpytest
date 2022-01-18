import pytest
import yaml
import sys
test_user_data = [{"user": "admin1", "psw": "111111"},
                  {"user": "admin2", "psw": "222"}]
@pytest.fixture()
def login(request):
    print("in login")
    user = request.param["user"]
    psw = request.param["psw"]
    print(user,psw)
    return user

@pytest.mark.parametrize("login",test_user_data,indirect = True)
# @pytest.mark.parametrize("login", test_user_data, indirect = True)
def test_1(login):
    print("test_1")


@pytest.mark.skip("buxiangzhixing")
def test_2():
    print("test_2")

@pytest.mark.skipif(sys.version >= "3.6",reason = "fff")
def test_3():
    print("test_3")

def test_4():
    print("test_4")
    pytest.skip("ddd")
    print("ddd-333")

@pytest.mark.xfail
def test_5():
    print("test_5")
    assert 1==2

@pytest.mark.parametrize("n",yaml.safe_load())
def test_6():
    print("test_6")