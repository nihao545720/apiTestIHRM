import json

import pymysql
from requests import Response
import app

#通用断言工具
def assert_common(self, response,http_code, success, code, message):
    '''
    @type response:Response
    '''
    jsonData = response.json() #type:dict
    # 断言返回状态码
    self.assertEqual(http_code, response.status_code)
    # 断言返回json数据中的success值
    self.assertEqual(success, jsonData.get("success"))
    # 断言返回的json数据中的code值
    self.assertEqual(code, jsonData.get("code"))
    # 断言返回的json 数据中的message值
    self.assertIn(message, jsonData.get("message"))

#连接数据库的封装
class DBUtils:
    def __init__(self,host,user,passwoed,database):
        self.conn = pymysql.connect(host,user,passwoed,database)

    def __enter__(self):
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    #__enter__和__exit__这两个魔法函数是python内置函数,是在使用with语法打开对象时,要执行的函数
    #执行顺序:with打开时,执行__enter__函数,退出with时<执行__exit__函数
    #with open(filename,mode="r") as f: pass
    #引用:with DBUtils() as db : db.execute()

#实现登录的数据
def read_login_data():
    login_data_path = app.BASE_DIR + "/data/login_data.json"
    with open(login_data_path,mode="r",encoding="utf-8") as f:
        jsonData = json.load(f)
        result_list = []
        for login_data in jsonData:
            mobile = login_data.get("mobile")
            password = login_data.get("password")
            http_code = login_data.get("http_code")
            success = login_data.get("success")
            code = login_data.get("code")
            message = login_data.get("message")
            result_list.append((mobile,password,http_code,success,code,message))
    print("result_list的值为:", result_list)
    return result_list

#实现添加的数据
def read_add_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path,mode="r",encoding="utf-8") as f:
        #使用json工具读取数据文件,加载成json的数据类型
        jsonData = json.load(f)
        result_list = []
        add_emp_data = jsonData.get("add_emp")
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        http_code = add_emp_data.get("http_code")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        result_list.append((username, mobile, http_code, success, code, message))
    print("add emp result_list的值为:", result_list)
    return result_list

#实现查询的数据
def read_query_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode="r", encoding="utf-8") as f:
        # 使用json工具读取数据文件,加载成json的数据类型
        jsonData = json.load(f)
        result_list = []
        query_emp_data = jsonData.get("query_emp")
        http_code = query_emp_data.get("http_code")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        result_list.append(( http_code, success, code, message))
    print("query emp result_list的值为:", result_list)
    return result_list

#实现修改的数据
def read_modify_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode="r", encoding="utf-8") as f:
        # 使用json工具读取数据文件,加载成json的数据类型
        jsonData = json.load(f)
        result_list = []
        read_modify_emp = jsonData.get("modify_emp")
        username = read_modify_emp.get("username")
        http_code = read_modify_emp.get("http_code")
        success = read_modify_emp.get("success")
        code = read_modify_emp.get("code")
        message = read_modify_emp.get("message")
        result_list.append((username, http_code, success, code, message))
    print("query emp result_list的值为:", result_list)
    return result_list

#实现删除的数据
def read_delete_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode="r", encoding="utf-8") as f:
        # 使用json工具读取数据文件,加载成json的数据类型
        jsonData = json.load(f)
        result_list = []
        read_delete_emp = jsonData.get("delete_emp")
        http_code = read_delete_emp.get("http_code")
        success = read_delete_emp.get("success")
        code = read_delete_emp.get("code")
        message = read_delete_emp.get("message")
        result_list.append((http_code, success, code, message))
    print("query emp result_list的值为:", result_list)
    return result_list

if __name__ == "__main__":
    read_login_data()



