# coding : utf-8
# @Time   :2020/6/13 21:25
# @Author :liu
# @Email  :704938465@qq.com
# @File   :handle_path.py


import os
DIR_PATH = os.path.dirname(__file__)
BASE_PATH = os.path.dirname(DIR_PATH)

LOGS_PATH = os.path.join(BASE_PATH, "logs")
DATA_PATH = os.path.join(BASE_PATH, "data")