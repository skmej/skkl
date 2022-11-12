# from selenium import webdriver
from po.page_home import HomeProxy
from po.page_login import LoginProxy
from utils import UtilsDriver,get_data
import time
import pytest
# import allure

# @allure.feature("登录功能")
class Test_login:
    def setup_class(self):
        self.login_p=LoginProxy()
        self.home_p=HomeProxy()
    def setup(self):
        # self.driver = webdriver.Chrome()

        # driver 是类属性 可以直接通过类名.driver获取
        # UtilsDriver.driver
        # self.driver = UtilsDriver.get_driver()
        # 进入首页
        UtilsDriver.get_driver().get("http://127.0.0.1:8080/")
        # self.driver.maximize_window()
        # 进入到login界面
        # self.driver.find_element_by_class_name("red").click()
        self.home_p.go_login_page()
    def teardown_class(self):
        time.sleep(2)
        UtilsDriver.quit_driver()

    # @pytest.mark.parametrize(["username","pwd","code","asrt_msg"],get_data())
    # @allure.story("登录用户名错误")
    @pytest.mark.skip(reason="不想运行")
    def test_login_username_error(self,username,pwd,code,asrt_msg):
        # self.driver.find_element_by_id("username").send_keys("1322222222")
        # self.driver.find_element_by_id("password").send_keys("123456")
        # self.driver.find_element_by_id("verify_code").send_keys("8888")
        # self.driver.find_element_by_name("sbtbutton").click()
        self.login_p.login(username,pwd,code)
        time.sleep(1)
        # 登录是否成功的预期结果
        res = UtilsDriver.get_msg()
        assert asrt_msg in res

    # @allure.story("登录密码错误")
    @pytest.mark.skip(reason="不想运行")
    def test_login_pwd(self):
        # self.driver.find_element_by_id("username").send_keys("13888888888")
        # self.driver.find_element_by_id("password").send_keys("12345")
        # self.driver.find_element_by_id("verify_code").send_keys("8888")
        # self.driver.find_element_by_name("sbtbutton").click()
        self.login_p.login("13888888888", "12345", "8888")
        time.sleep(1)
        res = UtilsDriver.get_msg()
        assert "密码" in res