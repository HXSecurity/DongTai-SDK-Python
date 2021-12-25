'''
Author: 饕餮
Date: 2021-12-24 10:56:26
version: 
LastEditors: 饕餮
LastEditTime: 2021-12-25 17:22:07
Description: Agent Object
'''
import json
from .BaseObejct import BaseObject

class DongTaiAgent(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Id(self):
        return self.TryGetValue("id")

    @property
    def Token(self):
        return self.TryGetValue("token")

    @property
    def ShortName(self):
        return self.TryGetValue("short_name")
        
    @property
    def Alias(self):
        return self.TryGetValue("alias")

    @property
    def StartUpTime(self):
        return self.TryGetValue("startup_time")

    @property
    def RegisterTime(self):
        return self.TryGetValue("register_time")

    @property
    def User(self):
        return self.TryGetValue("user")

    @property
    def Server(self):
        return self.TryGetValue("server")

    @property
    def IsRunning(self):
        return self.TryGetValue("is_running")

    @property
    def IsCoreRunning(self):
        return self.TryGetValue("is_core_running")

    @property
    def Control(self):
        return self.TryGetValue("control")

    @property
    def IsControl(self):
        return self.TryGetValue("is_control")

    @property
    def BindProjectId(self):
        return self.TryGetValue("bind_project_id")

    @property
    def ProjectName(self):
        return self.TryGetValue("project_name")

    @property
    def Online(self):
        return self.TryGetValue("online")

    @property
    def ProjectVersionId(self):
        return self.TryGetValue("project_version_id")

    @property
    def Language(self):
        return self.TryGetValue("language")

    @property
    def RunningStatus(self):
        return self.TryGetValue("running_status")

    @property
    def SystemLoad(self):
        tmpData = self.TryGetValue("system_load")
        if tmpData is not None:
            return json.dumps(tmpData)
        else:
            return {}

    @property
    def Owner(self):
        return self.TryGetValue("owner")

    @property
    def LastestName(self):
        return self.TryGetValue("latest_time")

    @property
    def Flow(self):
        return self.TryGetValue("flow")

    @property
    def ReportQueue(self):
        return self.TryGetValue("report_queue")

    @property
    def MethodQueue(self):
        return self.TryGetValue("method_queue")

    @property
    def ReplayQueue(self):
        return self.TryGetValue("replay_queue")

    

    
