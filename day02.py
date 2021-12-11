import HTMLTestRunner_PY3
import unittest
from ddt import data,unpack,ddt

@ddt
class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass ")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("teraDown")

    @data("asf")
    def testcase1(self, value):
        print("testcase1", value)
        self.assertEqual(1, 1)

    @data((1,2),(2,3))
    @unpack
    def testcase2(self, *value  ):
        print("testcase2", value[0], value[1])


if __name__ == '__main__':
    dis = unittest.defaultTestLoader.discover("./", "day02.py")
    # runner = HTMLTestRunner_PY3.HTMLTestRunner(open("a.html", "wb"), title="接口自动化测试")
    # runner.run(dis)
    unittest.TextTestRunner().run(dis)