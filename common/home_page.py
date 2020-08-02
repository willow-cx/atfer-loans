# coding : utf-8
# @Time   :2020/6/14 12:10
# @Author :liu
# @Email  :704938465@qq.com
# @File   :home_page.py
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver


    def get_user_msg(self):
        success_elem = self.driver.find_element(By.XPATH, "//a[@href='/Member/index.html']")
        actual_error_msg = success_elem.text

        return actual_error_msg
