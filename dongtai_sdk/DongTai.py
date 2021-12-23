'''
Author: 饕餮
Date: 2021-12-23 15:10:01
version: 
LastEditors: 饕餮
LastEditTime: 2021-12-23 19:34:20
Description: 入口
'''
from .base.DongTaiProject import DongTaiProject
from .DongTaiApi import DongTaiApi

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

