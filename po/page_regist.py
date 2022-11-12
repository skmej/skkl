from selenium.webdriver.common.by import By

from base.page_base import BasePage
# 界面层
class PageRegist(BasePage):
    # 账号元素
    def find_username(self):
        return self.driver.find_element_by_id("username")
        # return self.driver.find_element(*self.username)
        # return self.get_element(self.username)

    # 密码元素
    def find_pwd(self):
        return self.driver.find_element(By.ID, "password")# 密码元素

    def find_pwd2(self):
        return self.driver.find_element(By.ID, "password2")

    # 验证码元素
    def find_vcode(self):
        return self.driver.find_element_by_name("verify_code")

    def find_phone(self):
        return self.driver.find_element(By.NAME,"invite")

    def find_regist_btn(self):
        return self.driver.find_element(By.CLASS_NAME,"J_btn_agree")


# 处理层
class HandleRegist(object):
    def __init__(self):
        self.page_regist = PageRegist()

    def input_username(self,username):
        self.page_regist.find_username().send_keys(username)

    def input_pwd(self,pwd):
        self.page_regist.find_pwd().send_keys(pwd)

    def input_pwd2(self,pwd2):
        self.page_regist.find_pwd2().send_keys(pwd2)

    def input_vcode(self,code):
        self.page_regist.find_vcode().send_keys(code)

    def input_phone(self,phone):
        self.page_regist.find_phone().send_keys(phone)

    def click_regist_btn(self):
        self.page_regist.find_regist_btn().click()

# 业务层

class RegistPorxy(object):
    def __init__(self):
        self.handle_regist= HandleRegist()

    def phone_regist(self,username,pwd,pwd2,code,phone):
        self.handle_regist.input_username(username)
        self.handle_regist.input_vcode(code)
        self.handle_regist.input_pwd(pwd)
        self.handle_regist.input_pwd2(pwd2)
        self.handle_regist.input_phone(phone)
        self.handle_regist.click_regist_btn()