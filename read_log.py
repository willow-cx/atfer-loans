# coding : utf-8
# @Time   :2020/5/24 20:03
# @Author :liu
# @Email  :704938465@qq.com
# @File   :read_log.py

test_list = []
with open("data.log", encoding="utf-8") as file:
    item = file.readline()
    for item in file:
        test_list +=item
    pass


