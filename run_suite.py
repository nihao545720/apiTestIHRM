# 导包
import unittest
import time
import app
from script.test_ihrm_emp import TeatEmp
from script.test_ihrm_emp_parametrized import TeatEmpPa
from script.test_loginihrm import TestLoginIhrm

from tools.HTMLTestRunner import HTMLTestRunner

# 初始化测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestLoginIhrm))
suite.addTest(unittest.makeSuite(TeatEmpPa))
# 初始化测试报告的路径和名称
report_path = app.BASE_DIR + "/report/tpshop{}.html".format(time.strftime("%Y%m%d %H%M%S"))
with open(report_path, mode="wb") as f:
    # 初始化HTMLTestRunner
    runner = HTMLTestRunner(f, verbosity=1, description="测试登录接口和员工管理模块", title="IHRM人力资源管理系统的测试报告")
    # 使用runner运行测试套件
    runner.run(suite)
