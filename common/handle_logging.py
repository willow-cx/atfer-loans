# coding : utf-8
# @Time   :2020/6/13 20:26
# @Author :liu
# @Email  :704938465@qq.com
# @File   :handle_logging.py

import logging
import os
from config.config import LOGING_NAME
from common.handle_path import LOGS_PATH


class HandleLogging:
    def __init__(self, name=None):
        if name is None:
            self.logger = logging.getLogger("test_logger")
        else:
            self.logger = logging.getLogger(name)
        self.logger.setLevel("INFO")
        sh = logging.StreamHandler()
        sh.setLevel("ERROR")
        fh = logging.FileHandler(os.path.join(LOGS_PATH, LOGING_NAME), "a+", encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - [mas]: %(message)s - %(filename)s - %(lineno)d")
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    def get_logger(self):
        return self.logger


do_logging = HandleLogging().get_logger()

if __name__ == '__main__':
    do_logging = HandleLogging().get_logger()
    do_logging.error("这是一个错误的信息")
