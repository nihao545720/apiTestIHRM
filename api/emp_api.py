import requests
import app


class EmpApi():
    def __init__(self):
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"   #  员工管理的url

    def add_emp(self,username,mobile):
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2019-11-05",
            "formOfEmployment": 1,
            "workNumber": "111",
            "departmentName": "财务部",
            "departmentId": "1066238836272664576",
            "correctionTime": "2019-11-30"
            }
        return requests.post(self.emp_url, json=data, headers=app.HEADERS)


    #查询员工
    def query_emp(self):
        #拼接要发送的查询员工URL
        query_emp_url = self.emp_url + "/" + app.EMPID
        #发送查询员请求,并返回响应数据
        return requests.get(query_emp_url, headers=app.HEADERS)

    #修改员工
    def modify_emp(self,username):
        #拼接修改员工的url
        modify_emp_url = self.emp_url + "/" + app.EMPID

        #发送修改员工
        return requests.put(modify_emp_url,json={"username":username},headers=app.HEADERS)

    #删除员工
    def del_emp(self):
        #拼接员工的url
        del_emp_url = self.emp_url + "/" + app.EMPID

        #发送删除员工
        return requests.delete(del_emp_url,headers=app.HEADERS)


