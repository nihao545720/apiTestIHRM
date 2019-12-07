import logging
import unittest

from parameterized import parameterized

import app
from api.emp_api import EmpApi
from utils import assert_common, read_add_emp_data, DBUtils, read_query_emp_data, read_modify_emp_data, \
    read_delete_emp_data


class TeatEmpPa(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.emp_api = EmpApi()

        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    #添加员工
    @parameterized.expand(read_add_emp_data)
    def test01_emp(self,username,mobile,http_code,success,code,message):
        #调用添加员工接口
        response = self.emp_api.add_emp(username, mobile)
        logging.info("添加员工接口返回的数据为: {}".format(response.json()))

        #断言
        assert_common(self,response,http_code,success,code,message)

        #获取添加员工接口返回的json数据
        jsonData = response.json()
        #获取员工id
        emp_id = jsonData.get("data").get("id")
        #保存员工id到全局变量
        app.EMPID = emp_id
        #打印员工id
        logging.info("保存的员工id是: {}".format(app.EMPID))

        # 查询员工
    @parameterized.expand(read_query_emp_data)
    def test02_query_emp(self,http_code,success,code,message):
        # 调用查询员工接口
        response = self.emp_api.query_emp()
        logging.info("查询员工接口返回的数据为: {}".format(response.json()))

        # 断言
        assert_common(self, response, http_code, success, code, message)


     # 修改员工
    @parameterized.expand(read_modify_emp_data)
    def test03_modify_emp(self,username, http_code, success, code, message):
        # 调用修改员工接口
        response = self.emp_api.modify_emp(username)
        # 打印
        logging.info("修改员工返回的数据是: {}".format(response.json()))

        # 断言
        assert_common(self, response, http_code, success, code, message)
        # 断言数据库中的数据
        with DBUtils("182.92.81.159", "readuser", "iHRM_user_2019", "ihrm") as db:
            # 执行查询语句
            query_sql = "select username from bs_user where id={} limit 1".format(app.EMPID)
            db.execute(query_sql)
            result = db.fetchone()

            logging.info("--------查询数据库中的员工id为{}的username是:{}".format(app.EMPID, result[0]))
            # 断言
            self.assertEqual(username, result[0])



            # 删除员工
    @parameterized.expand(read_delete_emp_data)
    def test04_del_emp(self,http_code, success, code, message):
        # 调用删除员工接口
        response = self.emp_api.del_emp()
        # 打印
        logging.info("删除员工返回的数据是: {}".format(response.json()))

        # 断言
        assert_common(self, response, http_code, success, code, message)