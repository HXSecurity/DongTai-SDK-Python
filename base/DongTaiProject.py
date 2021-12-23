'''
Author: 饕餮
Date: 2021-12-23 14:50:44
version: 
LastEditors: 饕餮
LastEditTime: 2021-12-23 15:03:40
Description: 动态项目对象
'''
import json
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