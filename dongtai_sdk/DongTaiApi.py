'''
Author: 饕餮
Date: 2021-12-23 14:27:00
version: 
LastEditors: 饕餮
LastEditTime: 2021-12-24 11:08:06
Description: file content
'''
import json,requests
class DongTaiApi:
    def __init__(self,configPath='config.json'):
        with open(configPath, 'r') as config_f:
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

    #[Project Function]
    #获取项目列表
    def GetProjectList(self,page=1,pageSize=50,pName=None):
        data = {
            "page":page,
            "pageSize":pageSize
        }
        if pName is not None:
            data["name"] = pName
        return self.GetResponse("/projects","GET",data)

    #获取项目版本列表
    def GetProjectVerList(self,projectId):
        return self.GetResponse(f"/project/version/list/{projectId}")

    #项目版本添加
    def AddProjectVersion(self,projectId,verName,description,isEdit=True):
        data = {
            "version_name": verName,
            "description": description,
            "isEdit": isEdit,
            "project_id": projectId
        }
        return self.GetResponse("/project/version/add","POST",data=json.dumps(data))

    #项目搜索
    def SearchProject(self,projectId):
        return self.GetResponse(f"/api/v1/projects/summary/{projectId}")

    #[Agent Function]
    def DeleteAgent(self,agentId):
        pass

    def ModifiedAgentAlias(self,agentId,alias):
        pass

    def GetAgentList(self,page=1,pageSize=50,projectName=None,state=None,token=None):
        pass

    def StartAgent(self,agentId):
        pass

    def StopAgent(self,agentId):
        pass

    def GetAgentDetail(self,agentId):
        pass