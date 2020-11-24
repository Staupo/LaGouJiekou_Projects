# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 6:14 下午
# @Author  : Saber
# @FileName: test_wework_access.py
# @Software: PyCharm


import requests


class TestWeworkAccess:

    s = requests.session()
    def setup_token(self):
        params = {
            "corpid": "wwfd049f1c4668b481",
            "corpsecret": "5X85JObPEdg0np8c3veNYJwGahT7jnIXVq6qQj2fWqM"
        }
        r = self.s.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
        self.s.params.update({"access_token": r.json()['access_token']})

    def test_add_resion(self):
        data = {
            "userid": "caixukun",
            "name": "蔡徐坤",
            "mobile": "18099004523",
            "department": [1]
        }
        r = self.s.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create", json=data)
        self.s.params.update({"userid": "caixukun"})
        print(r.json())

    def test_get(self):
        params = {
            'userid': 'caixukun'
        }
        r = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",params=params)
        return r.json()
        print(r.json())

    def test_update(self):
        data = {
            "userid": "caixunkun",
            "name": "五选一"
        }
        r = self.s.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update",json=data)
        print(r.json())
        assert (self.test_get()['name'] == "五选一")

    def test_delete(self):
        params = {
            "userid": "caixukun",
            "access_token": "五选一"
        }
        r = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete", params=params)
        print(r.json())
        assert r.json()["errmsg"] == 'deleted'


