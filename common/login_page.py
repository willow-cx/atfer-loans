# coding : utf-8
# @Time   :2020/6/13 20:02
# @Author :liu
# @Email  :704938465@qq.com
# @File   :login_page.py

from config.config import HOST
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        """
        打开网址，窗口最大化，设置隐式等待时间
        """
        self.driver = driver

    def get(self):
        url = HOST + "/Index/login.html"
        self.driver.get(url)

    def test_login(self, username, password):
        """
        登录页面，元素定位和操作
        :param username: 用户名定位和操作
        :param password: 密码定位和操作
        :return:
        """
        username_elem = self.driver.find_element(By.NAME, "phone")
        username_elem.send_keys(username)
        # 定位密码，并输入空
        pwd_elem = self.driver.find_element(By.NAME, "password")
        pwd_elem.send_keys(password)
        # 定位登录
        login_elem = self.driver.find_element(By.XPATH, "//button[@class='btn btn-special']")
        login_elem.click()

    def test_login_error_msg(self):
        """
        登录时错误信息提示语
        :return:
        """
        error_elem = self.driver.find_element(By.XPATH, "//div[@class='form-error-info']")
        actual_error_msg = error_elem.text

        return actual_error_msg

    def invalid_error_msg(self):
        """
        没授权用户名登录提示语
        :return:
        """
        error_elem = WebDriverWait(self.driver, 20, 0.8).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='layui-layer-content']")))
        # error_elem = self.driver.find_element(By.XPATH, "//div[@class='layui-layer-content']")
        actual_error_msg = error_elem.text

        return actual_error_msg

