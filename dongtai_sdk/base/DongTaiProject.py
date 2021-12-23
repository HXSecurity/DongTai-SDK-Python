'''
Author: 饕餮
Date: 2021-12-23 14:50:44
version: 
LastEditors: 饕餮
LastEditTime: 2021-12-23 20:54:08
Description: 动态项目对象
'''
from .BaseObejct import BaseObject

class VulCount(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData
    
    @property
    def Level(self):
        return self.TryGetValue("level")

    @property
    def Total(self):
        return self.TryGetValue("total")

    @property
    def Name(self):
        return self.TryGetValue("name")

class DongTaiProjectVersion(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def VersionId(self):
        return self.TryGetValue("version_id")

    @property
    def VersionName(self):
        return self.TryGetValue("version_name")

    @property
    def CurrentVersion(self):
        return self.TryGetValue("current_version")

    @property
    def Description(self):
        return self.TryGetValue("description")

class DongTaiProject(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Id(self):
        return self.TryGetValue("id")

    @property
    def Name(self):
        return self.TryGetValue("name")

    @property
    def Mode(self):
        return self.TryGetValue("mode")

    @property
    def VulCount(self):
        tmpDataList = self.TryGetValue("vul_count")
        returnData = []
        for tmpData in tmpDataList:
            tmpObject = VulCount(tmpData)
            returnData.append(tmpObject)
        return returnData

    @property
    def AgentCount(self):
        return self.TryGetValue("agent_count")

    @property
    def Owner(self):
        return self.TryGetValue("owner_count")

    @property
    def LatestTime(self):
        return self.TryGetValue("latest_time")

    @property
    def AgentLanguage(self):
        return self.TryGetValue("agent_language")

    @property
    def VulValidation(self):
        return self.TryGetValue("vul_validation")