'''
Author: 饕餮
Date: 2021-12-23 14:27:00
version: 
LastEditors: 饕餮
LastEditTime: 2021-12-23 14:48:19
Description: file content
'''
import json,requests
class DongTaiApi:
    def __init__(self):
        with open('config.json', 'r') as config_f:
            Config = json.load(config_f)
            DongTaiConfig = Config['DongTai']
            self.Token = DongTaiConfig["token"]
            self.BaseUrl = DongTaiConfig["url"]

    def GetApiFileUrl(self, url):
        return self.BaseUrl + "/api/v1" + url

    def GetResponse(self, url, type="GET", tmpData=None):
        requestHeader = {"Authorization":f"Token {self.Token}"}
        if type == 'GET':
            rep = requests.get(self.GetApiFileUrl(url), params=tmpData,headers=requestHeader)
        elif type == 'POST':
            rep = requests.post(self.GetApiFileUrl(url), data=tmpData,headers=requestHeader)
        return json.loads(rep.text)

    #获取项目列表
    def GetProjectList(self,page=1,pageSize=50,pName=None):
        data = {
            "page":page,
            "pageSize":pageSize
        }
        if pName is not None:
            data["name"] = pName
        return self.GetResponse("/projects","GET",data)