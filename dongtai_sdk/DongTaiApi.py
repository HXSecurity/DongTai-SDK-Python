'''
Author: 饕餮
Date: 2021-12-23 14:27:00
version: 
LastEditors: 饕餮
LastEditTime: 2021-12-24 12:22:43
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
        return self.GetResponse("/project/version/add","POST",data)

    #项目搜索
    def SearchProject(self,projectId):
        return self.GetResponse(f"/projects/summary/{projectId}")

    #[Agent Function]
    #删除探针
    def DeleteAgent(self,agentId):
        return self.GetResponse(f"/agent/{agentId}/delete")

    #修改探针别名
    def ModifiedAgentAlias(self,agentId,alias):
        data = {
            "id":agentId,
            "alias":alias
        }
        return self.GetResponse("/agent/alias/modified","POST",data)
    
    #获取探针列表
    def GetAgentList(self,page=1,pageSize=50,projectName=None,state=None,token=None):
        data = {
            "page":page,
            "pageSize":pageSize
        }
        if projectName is not None:
            data["project_name"] = projectName
        if state is not None:
            data["state"] = state
        if token is not None:
            data["token"] = token
        return self.GetResponse("/agents","GET",data)

    #启动探针
    def StartAgent(self,agentId):
        data = {
            "id":agentId
        }
        return self.GetResponse("/agent/start","POST",data)

    #停止探针
    def StopAgent(self,agentId):
        data = {
            "id":agentId
        }
        return self.GetResponse("/agent/stop","POST",data)

    #探针详情
    def GetAgentDetail(self,agentId):
        return self.GetResponse(f"/agent/{agentId}")