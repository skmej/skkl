import logging
import logging.handlers
from selenium import webdriver
import time
import json
import xlrd

class UtilsDriver(object):
    # python 分类 类属性(类变量) 类方法(类函数) 和 实例属性(变量) 实例方法 头上有没有加classsmethon
    # 如果 不想让外部看见 方法或者属性 只需要在前面加上"_"
    # 加上"_" 方法或者属性就会变成私有方法或者属性
    _driver = None

    @classmethod
    def get_driver(cls):
        # 单例设计模式
        if cls._driver is None:
            cls._driver = webdriver.Chrome("./chromedriver.exe")
            cls._driver.maximize_window()
        return cls._driver

    @classmethod
    def quit_driver(cls):
        cls._driver.quit()
        cls._driver = None

    @classmethod
    def get_msg(cls):
        time.sleep(1)
        return cls._driver.find_element_by_class_name("layui-layer-content").text


# 获取登陆数据的方式
# [("139889888","123456","8888","账号格式不匹配"),("139889888","123456","8888","账号格式不匹配")]
def get_data(str):
    str = './data/login_username.json'
    with open(str,"r",encoding="utf8") as f:
        json_str = f.read()
        # 把json字符串转化为python对象
        json_py = json.loads(json_str)
        # print(json_py)
        datas = []
        for a in json_py:
            data = (a.get("username"),a.get("pwd"),a.get("code"),a.get("ast_msg"))
            datas.append(data)

        # print(datas)
        return datas

# 获取注册的输入条件
def get_regist_data(is_head =True):
    xlsx = xlrd.open_workbook("./data/regist_username.xlsx")
    # 获取工作表
    sheet = xlsx.sheet_by_index(0)
    datas = []
    for i in range(sheet.nrows):
        # [1:]是不是切片  去除掉我们exlc表格里的表头   就按我们这个格式来   不用变
        datas.append(sheet.row_values(i)[:-1])
    if is_head:
        datas = datas[1:]
    return datas
# 日志
def init_logger(logname):
    # 获取日志器
    logger = logging.getLogger(logname)

    # 设置日志输出级别
    logger.setLevel(logging.DEBUG)

    # 日志输出到哪里
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    # 设置输出格式
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    # 格式化器
    fmter = logging.Formatter(fmt=fmt)
    sh.setFormatter(fmter)

    fh = logging.handlers.TimedRotatingFileHandler("./log/log.log",when="midnight",interval=1,backupCount=0,encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmter)

    logger.addHandler(sh)
    logger.addHandler(fh)

    return logger


if __name__ == '__main__':
    print(get_regist_data())