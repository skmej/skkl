import logging
import logging.handlers
import time
def out_log():
    # 获取日志器
    logger = logging.getLogger("mylogger")

    # 设置日志输出级别
    logger.setLevel(logging.DEBUG)

    # 日志输出到哪里
    sh = logging.StreamHandler() # sh对象
    sh.setLevel(logging.DEBUG)
    # 设置输出格式
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    # 格式化器
    fmter = logging.Formatter(fmt=fmt)
    # 设置格式化输出
    sh.setFormatter(fmter)
                                            # 参数1，输出日志文件的位置，2，时间，按照时间分割日志，3根据2参数的时间单位
                                            # 4，表示留取多少文件数量，0表示不删除 5，编码格式
    fh = logging.handlers.TimedRotatingFileHandler("log/log.log", when="S", interval=20, backupCount=0, encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmter)

    logger.addHandler(sh)
    logger.addHandler(fh)

    return logger

#
# if __name__ == '__main__':
#     logger = out_log()
#
#     while True:
#         time.sleep(1)
#         logger.info("这是一个info类型的日志")