from selenium.webdriver.support.wait import WebDriverWait

from utils import UtilsDriver
class BasePage(object):

    def __init__(self):
        self.driver = UtilsDriver.get_driver()

        # 定义获取元素对象的方法

    # def get_element(self, location):
    #     wait = WebDriverWait(self.driver, 10, 1)
    #     element = wait.until(lambda x: x.find_element(*location))
    #     return element