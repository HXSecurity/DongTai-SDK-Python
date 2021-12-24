'''
Author: 饕餮
Date: 2021-12-23 15:10:01
version: 
LastEditors: 饕餮
LastEditTime: 2021-12-24 10:08:23
Description: Main
'''
from .base.DongTaiProject import DongTaiProject,DongTaiProjectVersion
from .DongTaiApi import DongTaiApi
from .base.BaseObejct import DongTaiError

class DongTai:
    def __init__(self,configPath='config.json'):
        self.dongTaiApi = DongTaiApi(configPath)

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

