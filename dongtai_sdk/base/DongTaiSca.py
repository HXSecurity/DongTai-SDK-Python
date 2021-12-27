'''
Author: 饕餮
Date: 2021-12-24 10:57:03
version: 
LastEditors: 饕餮
LastEditTime: 2021-12-27 11:38:07
Description: Sca Object
'''
import json
from .BaseObejct import BaseObject,ProjectSummary,LanguageSummary

class ScaVulnReference(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Type(self):
        return self.TryGetValue("type")

    @property
    def Title(self):
        return self.TryGetValue("title")

    @property
    def Url(self):
        return self.TryGetValue("url")

class ScaVuln(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def SafeVersion(self):
        return self.TryGetValue("safe_version")

    @property
    def VulCve(self):
        return self.TryGetValue("vulcve") 

    @property
    def VulCwe(self):
        return self.TryGetValue("vulcwe")

    @property
    def VulName(self):
        return self.TryGetValue("vulname")

    @property
    def OverView(self):
        return self.TryGetValue("overview")

    @property
    def TearDown(self):
        return self.TryGetValue("teardown")

    @property
    def Reference(self):
        returnData = []
        tmpData = self.TryGetValue("reference")
        if tmpData is not None:
            tmpDataList = json.dumps(tmpData)
            for tmpItem in tmpDataList:
                tmpObject = ScaVulnReference(tmpItem)
                returnData.append(tmpObject)
        return returnData

class ScaLevel(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Level(self):
        return self.TryGetValue("level")

    @property
    def Count(self):
        return self.TryGetValue("count")

    @property
    def LevelId(self):
        return self.TryGetValue("level_id")

class DongTaiSca(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Id(self):
        return self.TryGetValue("id")

    @property
    def PackageName(self):
        return self.TryGetValue("package_name")

    @property
    def Version(self):
        return self.TryGetValue("version")

    @property
    def ProjectName(self):
        return self.TryGetValue("project_name")

    @property
    def ProjectId(self):
        return self.TryGetValue("project_id")

    @property
    def ProjectVersion(self):
        return self.TryGetValue("project_version")

    @property
    def Language(self):
        return self.TryGetValue("language")

    @property
    def AgentName(self):
        return self.TryGetValue("agent_name")

    @property
    def SignatureValue(self):
        return self.TryGetValue("signature_value")

    @property
    def Level(self):
        return self.TryGetValue("level")

    @property
    def LevelType(self):
        return self.TryGetValue("level_type")

    @property
    def VulCount(self):
        return self.TryGetValue("vul_count")

    @property
    def Dt(self):
        return self.TryGetValue("dt")

    @property
    def Vuls(self):
        returnData = []
        tmpDataList = self.TryGetValue("vuls")
        if tmpDataList is not None:
            for tmpData in tmpDataList:
                tmpObject = ScaVuln(tmpData)
                returnData.append(tmpObject)
        return returnData

class ScaSummary(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Language(self):
        returnData = []
        tmpDataList = self.TryGetValue("language")
        if tmpDataList is not None:
            for tmpData in tmpDataList:
                tmpObject = LanguageSummary(tmpData)
                returnData.append(tmpObject)
        return returnData

    @property
    def Level(self):
        returnData = []
        tmpDataList = self.TryGetValue("level")
        if tmpDataList is not None:
            for tmpData in tmpDataList:
                tmpObject = ScaLevel(tmpData)
                returnData.append(tmpObject)
        return returnData

    @property
    def Projects(self):
        returnData = []
        tmpDataList = self.TryGetValue("projects")
        if tmpDataList is not None:
            for tmpData in tmpDataList:
                tmpObject = ProjectSummary(tmpData)
                returnData.append(tmpObject)
        return returnData