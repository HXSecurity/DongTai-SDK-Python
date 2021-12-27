'''
Author: 饕餮
Date: 2021-12-23 14:49:05
version: 
LastEditors: 饕餮
LastEditTime: 2021-12-27 11:37:36
Description: 通用基类
'''
import json

class BaseObject:
    def __init__(self):
        self.ObjectData = {}

    def TryGetValue(self,key,default=None):
        keyArray = key.split('.')
        keyStr = ""
        #key内容为字典的不存在则返回默认
        if len(keyArray) > 0:
            baseDic = self.ObjectData
            for k in keyArray[0:len(keyArray)]:
                if k not in baseDic.keys():
                    return default
                baseDic = baseDic[k]
        #key栈组装
        for k in keyArray:
            keyStr +="['{0}']".format(k)
        #数据赋值
        return eval("self.ObjectData" + keyStr)

    def SetValue(self,key,value):
        keyArray = key.split('.')
        keyStr = ""
        #key内容为字典的不存在则建立
        if len(keyArray) > 1:
            baseDic = self.ObjectData
            for k in keyArray[0:len(keyArray)-1]:
                if k not in baseDic.keys():
                    baseDic[k] = {}
                baseDic = baseDic[k]
        #key栈组装
        for k in keyArray:
            keyStr +="['{0}']".format(k)
        #数据赋值
        exec("self.ObjectData" + keyStr + "=value")

    def is_json(self,jsonStr):
        try:
            json_object = json.loads(jsonStr)
        except ValueError as e:
            return False
        return True

class DongTaiError(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Status(self):
        return self.TryGetValue("status")

    @property
    def ErrorMsg(self):
        return self.TryGetValue("msg")

class ProjectSummary(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData
    
    @property
    def ProjectName(self):
        return self.TryGetValue("project_name")

    @property
    def Count(self):
        return self.TryGetValue("count")

    @property
    def Id(self):
        return self.TryGetValue("id")

class LanguageSummary(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Language(self):
        return self.TryGetValue("language")

    @property
    def Count(self):
        return self.TryGetValue("count")