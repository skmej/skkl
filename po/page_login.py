from selenium.webdriver.common.by import By

from utils import UtilsDriver
from base.page_base import BasePage


# 界面对象层

class PageLogin(BasePage):
    # def __init__(self):
    # #     #  self.driver = UtilsDriver.get_driver()
    #     BasePage.__init__(self)
    # #     # super().__init__(self)\
    #     self.username = By.ID,"username"


    # 账号元素
    def find_username(self):
        return self.driver.find_element_by_id("username")
        # return self.driver.find_element(*self.username)
        # return self.get_element(self.username)

    # 密码元素
    def find_pwd(self):
        return self.driver.find_element(By.ID,"password")

    # 验证码元素
    def find_vcode(self):
        return self.driver.find_element_by_id("verify_code")

    # 按钮开始登录元素
    def find_login_btn(self):
        # return self.driver.find_element_by_name("sbtbutton")
        return self.driver.find_element(By.NAME,"sbtbutton")

# 操作层
class HandleLogin(object):
    def __init__(self):
        self.page_login=PageLogin()

    def input_username(self,username):
        self.page_login.find_username().send_keys(username)

    def input_pwd(self,pwd):
        self.page_login.find_pwd().send_keys(pwd)

    def input_vcode(self,code):
        self.page_login.find_vcode().send_keys(code)

    def click_login_btn(self):
        self.page_login.find_login_btn().click()

# 业务层
# 输入用户名密码验证码 点击登录
class LoginProxy(object):
    def __init__(self):
        self.handle_login = HandleLogin()

    def login(self,username,pwd,code):
        self.handle_login.input_username(username)
        self.handle_login.input_pwd(pwd)
        self.handle_login.input_vcode(code)
        self.handle_login.click_login_btn()