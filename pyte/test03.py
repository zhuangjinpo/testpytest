import pytest


class TestDemo():

    def test1(self):
        print("执行test1方法")
        x = "this"
        pytest.assume(2 == 2)
        pytest.assume(8 == 8)
        # assert "t" in x

    def test2(self):
        print("执行test2方法")
        assert 1 == 1

    def test3(self):
        print("执行test3方法")

if __name__ == '__main__':
    pytest.main("-v -s day03.py::TestDemo")
    # pytest.main(["-v","-s","TestDemo"])
