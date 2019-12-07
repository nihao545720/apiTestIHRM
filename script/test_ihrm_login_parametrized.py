
#参数化执行用例
# 导包
import logging
import unittest

from parameterized import parameterized

from api.loginapi import LoginApi
from utils import assert_common, read_login_data


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

    @parameterized.expand(read_login_data)
    def test01_login(self,mobile,password,http_code,success,code,message):
        # 发送登录请求
        response = self.login_api.login(mobile, password)
        # 打印日志
        logging.info("登录接口返回的数据为:{}".format(response.json()))
        # 断言
        assert_common(self, response, http_code, success, code, message)
