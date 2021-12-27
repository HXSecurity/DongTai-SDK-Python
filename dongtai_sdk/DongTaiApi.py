'''
Author: 饕餮
Date: 2021-12-23 14:27:00
version: 
LastEditors: 饕餮
LastEditTime: 2021-12-27 17:03:50
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
    #项目版本修改
    def ChangeProjectVersion(self,projectId,versionId):
        data = {
            "version_id":versionId,
            "project_id":projectId
        }
        return self.GetResponse("/project/version/current","POST",data)

    #删除项目
    def DeleteProject(self,projectId):
        data = {
            "id":projectId
        }
        return self.GetResponse("/project/delete","POST",data)

    #项目版本更新
    def UpdateProjectVersion(self,projectId,versionName,versionId,description,currentVersion=1,isEdit=True):
        data = {
            "version_name": versionName,
            "description": description,
            "isEdit": isEdit,
            "version_id": versionId,
            "current_version": currentVersion,
            "project_id": projectId
        }
        return self.GetResponse("/project/version/update","POST",data)

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

    #项目探针列表
    def GetProjectAgentList(self,projectId):
        return self.GetResponse(f"/project/engines/{projectId}")

    #获取项目详情
    def GetProjectDetail(self,projectId):
        return self.GetResponse(f"/project/{projectId}")


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

    #[Sca Function]
    #组件概况
    def GetScaSummary(self,page=1,pageSize=50,keyword=None,language=None,level=None,order=None,projectId=None,projectName=None,versionId=None):
        data = {
            "page":page,
            "pageSize":pageSize
        }
        if keyword is not None:
            data["keyword"] = keyword
        if language is not None:
            data["language"] = language
        if level is not None:
            data["level"] = level
        if order is not None:
            data["order"] = order
        if projectId is not None:
            data["project_id"] = projectId
        if projectName is not None:
            data["project_name"] = projectName
        if versionId is not None:
            data["version_id"] = versionId
        return self.GetResponse("/sca/summary","GET",data)

    #组件列表
    def GetScaList(self,page=1,pageSize=50,keyword=None,language=None,level=None,order=None,projectId=None,projectName=None,versionId=None):
        data = {
            "page":page,
            "pageSize":pageSize
        }
        if keyword is not None:
            data["keyword"] = keyword
        if language is not None:
            data["language"] = language
        if level is not None:
            data["level"] = level
        if order is not None:
            data["order"] = order
        if projectId is not None:
            data["project_id"] = projectId
        if projectName is not None:
            data["project_name"] = projectName
        if versionId is not None:
            data["version_id"] = versionId
        return self.GetResponse("/scas","GET",data)

    #组件详情
    def GetScaDetail(self,scaId):
        return self.GetResponse(f"/sca/{scaId}")

    #[Vuln Function]
    #漏洞概览
    def GetVulnSummary(self,projectId=None,language=None,level=None,order=None,projectName=None,status=None,type=None,url=None,versionId=None,statusId=None):
        data = {}
        if projectId is not None:
            data["project_id"] = projectId
        if statusId is not None:
            data["status_id"] = statusId
        if language is not None:
            data["language"] = language
        if level is not None:
            data["level"] = level
        if order is not None:
            data["order"] = order
        if projectName is not None:
            data["project_name"] = projectName
        if versionId is not None:
            data["version_id"] = versionId
        if status is not None:
            data["status"] = status
        if type is not None:
            data["type"] = type
        if url is not None:
            data["url"] = url
        return self.GetResponse("/vuln/summary","GET",data)

    #漏洞详情
    def GetVulnDetail(self,vulnId):
        return self.GetResponse(f"/vuln/{vulnId}")

    #漏洞验证
    def RecheckVuln(self,vulnIdList):
        data = {
            "ids": ",".join([str(id) for id in vulnIdList])
        }
        return self.GetResponse("/vul/recheck","POST",data)

    