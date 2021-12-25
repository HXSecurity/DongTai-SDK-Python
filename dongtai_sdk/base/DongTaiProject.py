'''
Author: 饕餮
Date: 2021-12-23 14:50:44
version: 
LastEditors: 饕餮
LastEditTime: 2021-12-25 16:06:03
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

class AgentBaseInfo(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Id(self):
        return self.TryGetValue("id")

    @property
    def Name(self):
        return self.TryGetValue("name")

class LevelCount(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def LevelId(self):
        return self.TryGetValue("level_id")

    @property
    def LevelName(self):
        return self.TryGetValue("level_name")

    @property
    def Number(self):
        return self.TryGetValue("num")

class DayNumber(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def DayLabel(self):
        return self.TryGetValue("day_label")
    
    @property
    def DayNum(self):
        return self.TryGetValue("day_num")

class TypeSummary(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def TypeName(self):
        return self.TryGetValue("type_name")

    @property
    def TypeCount(self):
        return self.TryGetValue("type_count")

    @property
    def TypeLevel(self):
        return self.TryGetValue("type_level")

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

    @property
    def VersionData(self):
        tmpData = self.TryGetValue("versionData",None)
        if tmpData is not None:
            tmpObject = DongTaiProjectVersion(tmpData)
            return tmpObject
        else:
            return None

    @property
    def LevelCount(self):
        tmpDataList = self.TryGetValue("level_count")
        returnData = []
        for tmpData in tmpDataList:
            tmpObject = LevelCount(tmpData)
            returnData.append(tmpObject)
        return returnData

    @property
    def DayNumber(self):
        tmpDataList = self.TryGetValue("day_num")
        returnData = []
        for tmpData in tmpDataList:
            tmpObject = DayNumber(tmpData)
            returnData.append(tmpObject)
        return returnData

    @property
    def TypeSummary(self):
        tmpDataList = self.TryGetValue("type_summary")
        returnData = []
        for tmpData in tmpDataList:
            tmpObject = TypeSummary(tmpData)
            returnData.append(tmpObject)
        return returnData

    @property
    def ScanId(self):
        return self.TryGetValue("scan_id")
    
    #通过参数判断是否要加载完整的Agent信息
    @property
    def Agents(self):
        tmpDataList = self.TryGetValue("agents")
        returnData = []
        for tmpData in tmpDataList:
            tmpObject = AgentBaseInfo(tmpData)
            returnData.append(tmpObject)
        return returnData