'''
Author: 饕餮
Date: 2021-12-23 15:10:01
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-18 18:21:09
Description: Main
'''
from .base.DongTaiVuln import VulnDetail, VulnSummary
from .base.DongTaiProject import DongTaiProject,DongTaiProjectVersion
from .base.DongTaiAgent import DongTaiAgent
from .base.DongTaiSca import DongTaiSca, ScaSummary
from .DongTaiApi import DongTaiApi
from .base.BaseObejct import DongTaiError

class DongTai:
    def __init__(self,configPath='config.json'):
        self.dongTaiApi = DongTaiApi(configPath)

    #[Project Function]
    def GetProjectList(self,page,pageSize,name=None):
        returnData = []
        repData = self.dongTaiApi.GetProjectList(page,pageSize,name)
        if repData["status"] == 201:
            for tmpData in repData["data"]:
                tmpObject = DongTaiProject(tmpData)
                returnData.append(tmpObject)
            return returnData
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    def GetProjectVerList(self,projectId):
        returnData = []
        repData = self.dongTaiApi.GetProjectVerList(projectId)
        if repData["status"] == 201:
            for tmpData in repData["data"]:
                tmpObject = DongTaiProjectVersion(tmpData)
                returnData.append(tmpObject)
            return returnData
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    def DeleteProject(self,projectId):
        repData = self.dongTaiApi.DeleteProject(projectId)
        if repData["status"] == 201:
            return True
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    #TODO:获取项目版本详细信息如果参数不填自动填写原来的值
    def UpdateProjectVersion(self,projectId,versionName,versionId,description,currentVersion=1,isEdit=True):
        repData = self.dongTaiApi.UpdateProjectVersion(projectId,versionName,versionId,description,currentVersion,isEdit)
        if repData["status"] == 201:
            return True
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    def AddProjectVersion(self,projectId,verName,description,isEdit=True):
        repData = self.dongTaiApi.AddProjectVersion(projectId,verName,description,isEdit)
        if repData["status"] == 201:
            tmpObject = DongTaiProjectVersion(repData["data"])
            return tmpObject
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    def SearchProject(self,projectId):
        repData = self.dongTaiApi.SearchProject(projectId)
        if repData["status"] == 201:
            tmpObject = DongTaiProject(repData["data"])
            return tmpObject
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    def GetProjectDetail(self,projectId):
        repData = self.dongTaiApi.GetProjectDetail(projectId)
        if repData["status"] == 201:
            tmpObject = DongTaiProject(repData["data"])
            #TODO:通过参数判断是否加载完整Agent信息
            return tmpObject
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    def GetProjectAgentList(self,projectId):
        returnData = []
        repData = self.dongTaiApi.GetProjectAgentList(projectId)
        if repData["status"] == 201:
            tmpDataList = repData["data"]
            for tmpData in tmpDataList:
                tmpObect = DongTaiAgent(tmpData)
                returnData.append(tmpObect)
            return returnData
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    #[Agent Function]
    def DeleteAgent(self,agentId):
        repData = self.dongTaiApi.DeleteAgent(agentId)
        if repData["status"] == 201:
            return True
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    def StartAgent(self,agentId):
        repData = self.dongTaiApi.StartAgent(agentId)
        if repData["status"] == 201:
            return True
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    def StopAgent(self,agentId):
        repData = self.dongTaiApi.StartAgent(agentId)
        if repData["status"] == 201:
            return True
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    def ModifiedAgentAlias(self,agentId,alias):
        repData = self.dongTaiApi.ModifiedAgentAlias(agentId,alias)
        if repData["status"] == 201:
            return True
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    def GetAgentDetail(self,agentId):
        repData = self.dongTaiApi.GetAgentDetail(agentId)
        if repData["status"] == 201:
            agentObject = DongTaiAgent(repData["data"]["agent"])
            return agentObject
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    def GetAgentList(self,page=1,pageSize=50,projectName=None,state=None,token=None):
        returnData = []
        repData = self.dongTaiApi.GetAgentList(page,pageSize,projectName,state,token)
        if repData["status"] == 201:
            tmpDataList = repData["data"]
            for tmpData in tmpDataList:
                tmpObject = DongTaiAgent(tmpData)
                returnData.append(tmpObject)
            return returnData
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    #[Sca Function]
    def GetScaList(self,page=1,pageSize=50,keyword=None,language=None,level=None,order=None,projectId=None,projectName=None,versionId=None):
        returnData = []
        repData = self.dongTaiApi.GetScaList(self,page,pageSize,keyword,language,level,order,projectId,projectName,versionId)
        if repData["status"] == 201:
            tmpDataList = repData["data"]
            for tmpData in tmpDataList:
                tmpObject = DongTaiSca(tmpData)
                returnData.append(tmpObject)
            return returnData
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    def GetScaDetail(self,scaId):
        repData = self.dongTaiApi.GetScaDetail(scaId)
        if repData["status"] == 201:
            scaObject = DongTaiSca(repData["data"])
            return scaObject
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    def GetScaSummary(self,page=1,pageSize=50,keyword=None,language=None,level=None,order=None,projectId=None,projectName=None,versionId=None):
        repData = self.dongTaiApi.GetScaSummary(page,pageSize,keyword,language,level,order,projectId,projectName,versionId)
        if repData["status"] == 201:
            scaSummary = ScaSummary(repData["data"])
            return scaSummary
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    #[Vuln Function]
    def GetVulnSummary(self,projectId=None,language=None,level=None,order=None,projectName=None,status=None,type=None,url=None,versionId=None,statusId=None):
        repData = self.dongTaiApi.GetVulnSummary(projectId,language,level,order,projectName,status,type,url,versionId,statusId)
        if repData["status"] == 201:
            vulnSummary = VulnSummary(repData["data"])
            return vulnSummary
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject

    def GetVulnDetail(self,vulnId):
        repData = self.dongTaiApi.GetVulnDetail(vulnId)
        if repData["status"] == 201:
            vulnDetail = VulnDetail(repData["data"])
            return vulnDetail
        else:
            errorMsg = {"status":repData["status"],"msg":repData["msg"]}
            errorObject = DongTaiError(errorMsg)
            return errorObject
    
