import requests


class LoginApi:
    def __init__(self):
        self.login_url = "http://182.92.81.159" + "/api/sys/login"
        self.headers = {"Content-Type": "application/json"}

    def login(self, mobile, password):
        login_data = {"mobile": mobile, "password": password}
        return requests.post(self.login_url, json=login_data, headers=self.headers)

    #无参的情况
    def login_none_params(self):
        return requests.post(self.login_url, headers=self.headers)

    #多参的情况
    def login_extra_parmas(self):
        return requests.post(self.login_url,json={"mobile": "13800000002", "password": "123456", "extra":"测试"}, headers=self.headers)


    #少参的情况
    def login_less_parmas(self):
        return requests.post(self.login_url,json={"password": "123456",}, headers=self.headers)
