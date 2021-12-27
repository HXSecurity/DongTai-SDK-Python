'''
Author: 饕餮
Date: 2021-12-24 10:56:10
version: 
LastEditors: 饕餮
LastEditTime: 2021-12-27 18:55:58
Description: Vuln Object
'''
import json
from typing import List
from .BaseObejct import BaseObject,ProjectSummary,LanguageSummary

class VulnType(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Type(self):
        return self.TryGetValue("type")

    @property
    def Count(self):
        return self.TryGetValue("count")

class VulnLevel(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Level(self):
        return self.TryGetValue("level")

    @property
    def Count(self):
        return self.TryGetValue("count")

    @property
    def Id(self):
        return self.TryGetValue("level_id")

class VulnSummary(BaseObject):
    WithOutRiskLevel = ["无风险"]

    def __init__(self,jsonData,withOutRiskLevel:list=None):
        self.ObjectData = jsonData
        if withOutRiskLevel is not None:
            self.WithOutRiskLevel = withOutRiskLevel

    @property
    def Language(self) -> List[LanguageSummary]:
        returnData = []
        tmpDataList = self.TryGetValue("language")
        for tmpData in tmpDataList:
            tmpObject = LanguageSummary(tmpData)
            returnData.append(tmpObject)
        return returnData
        
    @property
    def Level(self) -> List[VulnLevel]:
        returnData = []
        tmpDataList = self.TryGetValue("level")
        for tmpData in tmpDataList:
            tmpObject = VulnLevel(tmpData)
            returnData.append(tmpObject)
        return returnData

    @property
    def Projects(self) -> List[ProjectSummary]:
        returnData = []
        tmpDataList = self.TryGetValue("projects")
        for tmpData in tmpDataList:
            tmpObject = ProjectSummary(tmpData)
            returnData.append(tmpObject)
        return returnData

    @property
    def HighRisk(self):
        tmpData = [tmpLevel for tmpLevel in self.Level if tmpLevel.Level == "高危"]
        if len(tmpData) > 0:
            return tmpData[0]
        else:
            return None

    @property
    def MediumRisk(self):
        tmpData = [tmpLevel for tmpLevel in self.Level if tmpLevel.Level == "中危"]
        if len(tmpData) > 0:
            return tmpData[0]
        else:
            return None

    @property
    def LowRisk(self):
        tmpData = [tmpLevel for tmpLevel in self.Level if tmpLevel.Level == "低危"]
        if len(tmpData) > 0:
            return tmpData[0]
        else:
            return None

    @property
    def TipsRisk(self):
        tmpData = [tmpLevel for tmpLevel in self.Level if tmpLevel.Level == "提示"]
        if len(tmpData) > 0:
            return tmpData[0]
        else:
            return None

    @property
    def Count(self):
        tmpCount = 0
        for tmpLevel in self.Level:
            if tmpLevel.Level not in self.WithOutRiskLevel:
                tmpCount += tmpLevel.Count
        return tmpCount


    

    