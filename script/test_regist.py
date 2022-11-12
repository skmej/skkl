import allure

from utils import UtilsDriver, get_regist_data, init_logger
from po.page_home import HomeProxy
from po.page_regist import RegistPorxy
import time
import pytest


# import allure


# @allure.feature("注册功能")
class Test_Resgist:

    def setup_class(self):
        self.logger = init_logger("register")

    def teardown_class(self):
        pass

    def setup(self):
        UtilsDriver.get_driver().get("http://localhost:8080/")
        self.home_p = HomeProxy()
        self.regist_p = RegistPorxy()
        # 进入到注册页面
        self.home_p.go_regist_page()
        UtilsDriver.get_driver().implicitly_wait(10)

    def teardown(self):
        UtilsDriver.quit_driver()
        pass

    # @allure.story("注册用户名错误")
    @pytest.mark.parametrize(['username', 'pwd', 'pwd2', 'code', 'phone', 'ast_msg'], get_regist_data())
    def test_regist_username_error(self, username, pwd, pwd2, code, phone, ast_msg):
        data_info = "username:{},pwd:{},pwd2:{},phone:{},ast_msg:{}".format(username, pwd, pwd2, phone, ast_msg)
        self.regist_p.phone_regist(username, pwd, pwd2, code, phone)
        time.sleep(2)
        with allure.step("获取提示弹框信息"):
            msg = UtilsDriver.get_msg()
        data_info = data_info + ",msg{}".format(msg)
        self.logger.info(data_info)
        with allure.step("断言"):
            assert ast_msg in msg
