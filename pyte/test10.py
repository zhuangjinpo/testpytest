import pytest
import allure
from allure_commons._allure  import  LinkType

from pyte.test03 import TestDemo


@allure.feature("第一个测试")
class Test_case():

    @allure.story("测试成功")
    # @allure.description("这是成功的测试描述")
    @allure.title("这是测试标题")
    @allure.issue("http://www.baidu.com","测试bug链接")
    @allure.testcase("http://www.tencent.com","测试用例链接")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_succ(self):
        """
        这是第二种测试描述
        :return:
        """
        with allure.step("打开浏览器"):
            print("打开浏览器")
        print("test_succ")
        allure.attach("./test09.py","sdf",allure.attachment_type.TEXT)
        allure.attach.file("./test09.py",attachment_type=allure.attachment_type.TEXT)

    def test_failure(self):
        print("test_failure")

    @allure.step("第二个步骤")
    def test_skip(self):
        print("test_skip")

