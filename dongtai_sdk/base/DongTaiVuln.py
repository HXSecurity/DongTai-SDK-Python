'''
Author: 饕餮
Date: 2021-12-24 10:56:10
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-18 18:20:18
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

class Vuln(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Url(self):
        return self.TryGetValue("url")

    @property
    def Uri(self):
        return self.TryGetValue("uri")

    @property
    def AgentName(self):
        return self.TryGetValue("agent_name")

    @property
    def HttpMethod(self):
        return self.TryGetValue("http_method")

    @property
    def Type(self):
        return self.TryGetValue("type")

    @property
    def TaintPosition(self):
        return self.TryGetValue("taint_position")

    @property
    def FirstTime(self):
        return self.TryGetValue("first_time")

    @property
    def LatestTime(self):
        return self.TryGetValue("latest_time")

    @property
    def ProjectName(self):
        return self.TryGetValue("project_name")

    @property
    def ProjectVersion(self):
        return self.TryGetValue("project_version")

    @property
    def Language(self):
        return self.TryGetValue("language")

    @property
    def Level(self):
        return self.TryGetValue("level")

    @property
    def LevelType(self):
        return self.TryGetValue("level_type")

    @property
    def Counts(self):
        return self.TryGetValue("counts")

    @property
    def ReqHeader(self):
        return self.TryGetValue("req_header")

    @property
    def Response(self):
        return self.TryGetValue("response")

    @property
    def Graph(self):
        return self.TryGetValue("graph")

    @property
    def ContextPath(self):
        return self.TryGetValue("context_path")

    @property
    def ClientIp(self):
        return self.TryGetValue("client_ip")

    @property
    def Status(self):
        return self.TryGetValue("status")

    @property
    def TaintValue(self):
        return self.TryGetValue("taint_value")

    @property
    def ParamName(self):
        return self.TryGetValue("param_name")

    @property
    def MethodPoolId(self):
        return self.TryGetValue("method_pool_id")

    @property
    def ProjectId(self):
        return self.TryGetValue("project_id")

class VulnServer(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Name(self):
        return self.TryGetValue("name")

    @property
    def Hostname(self):
        return self.TryGetValue("hostname")

    @property
    def Ip(self):
        return self.TryGetValue("ip")

    @property
    def Port(self):
        return self.TryGetValue("port")

    @property
    def Container(self):
        return self.TryGetValue("container")

    @property
    def ServerType(self):
        return self.TryGetValue("server_type")

    @property
    def ContainerPath(self):
        return self.TryGetValue("container_path")

    @property
    def Runtime(self):
        return self.TryGetValue("runtime")

    @property
    def Environment(self):
        return self.TryGetValue("environment")

    @property
    def Command(self):
        return self.TryGetValue("command")

class VulnDetail(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Vuln(self) -> Vuln:
        tmpData = self.TryGetValue("vul")
        tmpObject = Vuln(tmpData)
        return tmpObject

    @property
    def Server(self) -> VulnServer:
        tmpData = self.TryGetValue("server")
        tmpObject = VulnServer(tmpData)
        return tmpObject

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


    

    