import logging


fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
def add_log():
    # 日志模块的基本配置函数  ( 设置警告的级别 ,  我们输出信息的格式话  )
    logging.basicConfig(level=logging.DEBUG,format=fmt,filename='log/a.log')
    def input_username(self,username):
        self.page_login.find_username().send_keys(username)

    def input_pwd(self,pwd):
        self.page_login.find_pwd().send_keys(pwd)

    logging.debug("这是一个debug级别的日志")
    logging.info("这是一个info级别的日志")
    logging.warning("这是一个warning级别的日志")
    def input_vcode(self,code):
        self.page_login.find_vcode().send_keys(code)

    def click_login_btn(self):
        self.page_login.find_login_btn().click()


    logging.error("这是一个error级别的日志")
    logging.critical("这是一个critical级别的日志")

add_log()