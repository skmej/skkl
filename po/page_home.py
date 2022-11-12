# from utils import UtilsDriver
# 页面对象层
# 界面 找到首页需要的所有的元素
from base.page_base import BasePage

class PageHome(BasePage):
    # def __init__(self):
    #     self.driver = UtilsDriver.get_driver()

    def find_login_btn(self):
        return self.driver.find_element_by_link_text("登录")

    def find_regist_btn(self):
        return self.driver.find_element_by_link_text("注册")


# 操作层
# 操作每个元素

class HandleHome(object):
    def __init__(self):
        self.page_home = PageHome()

    def click_login_btn(self):
        self.page_home.find_login_btn().click()

    def click_regist_btn(self):
        self.page_home.find_regist_btn().click()

# 业务层
# 页面具体要干的事情
class HomeProxy(object):

    def __init__(self):
        self.hanlde_home  = HandleHome()

    def go_login_page(self):
        self.hanlde_home.click_login_btn()

    def go_regist_page(self):
        self.hanlde_home.click_regist_btn()
