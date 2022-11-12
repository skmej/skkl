import allure

def open_file():
    print("打开浏览器")

def input_data():
    print("输入数据")

@allure.feature("allure测试")
class TestAllure:

    def setup(self):
        print('---> setup')

    def teardown(self):
        print('teardown')

    @allure.story("测试a")
    def test_a(self):
        print('test_a')
        with allure.step("打开浏览器"):
            open_file()
            allure.attach("浏览器打开了首页","打开首页信息")

        with allure.step("输入数据"):
            input_data()
            allure.attach("手机号码:13888888,pwd:123456","数据")
        assert True

    @allure.story("测试b")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b(self):
        print('test_')
        assert False