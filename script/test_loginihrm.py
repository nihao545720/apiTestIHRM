# 导包
import logging
import unittest

import app
from api.loginapi import LoginApi
from utils import assert_common


class TestLoginIhrm(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    # 登录成功的测试用例
    def test01_login_success(self):
        # 发送登录请求
        response = self.login_api.login("13800000002", "123456")
        # 打印日志
        logging.info("登录接口返回的数据为:{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功")

        #获取json的数据
        jsonData = response.json()
        #拼接token组成全局变量
        token = "Bearer " + jsonData.get("data")
        #把token值保存到全局变量aap.py中
        #首先在app.py中创建HEADERS 变量才能保存
        app.HEADERS = {"Content-Type":"application/json", "Authorization":token}
        logging.info("保存的登录token和content-type: {}".format(app.HEADERS))


    # 账户不存在的测试用例
    def test02_mobile_is_error(self):
        # 发送登录请求
        response = self.login_api.login("13900000002", "123456")
        # 打印日志
        logging.info("登录接口返回的数据为:{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码错误的测试用例
    def test03_password_is_error(self):
        # 发送登录请求
        response = self.login_api.login("13800000002", "error")
        # 打印日志
        logging.info("登录接口返回的数据为:{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    # 无参的测试用例
    def test04_none_params(self):
        # 发送登录请求
        response = self.login_api.login_none_params()
        # 打印日志
        logging.info("登录接口返回的数据为:{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")

    #用户名为空测试用例
    def test05_mobile_is_null(self):
        # 发送登录请求
        response = self.login_api.login("", "error")
        # 打印日志
        logging.info("登录接口返回的数据为:{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")


    #密码为空测试用例
    def test06_password_is_null(self):
        # 发送登录请求
        response = self.login_api.login("13800000002", "")
        # 打印日志
        logging.info("登录接口返回的数据为:{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    #多参的测试
    def test07_extra_params(self):
        # 发送登录请求
        response = self.login_api.login_extra_parmas()
        # 打印日志
        logging.info("登录接口返回的数据为:{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功")

    #少参的测试用例
    def test08_less_parmas(self):
        # 发送登录请求
        response = self.login_api.login_less_parmas()
        # 打印日志
        logging.info("登录接口返回的数据为:{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")

