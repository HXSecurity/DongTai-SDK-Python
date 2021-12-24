<!--
 * @Author: 饕餮
 * @Date: 2021-12-23 14:25:35
 * @version: 
 * @LastEditors: 饕餮
 * @LastEditTime: 2021-12-24 13:00:32
 * @Description: How to use
-->
# DongTai-SDK-Python

[![license Apache-2.0](https://img.shields.io/github/license/HXSecurity/DongTai-SDK-Python)](https://github.com/HXSecurity/DongTai-SDK-Python/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/HXSecurity/DongTai-SDK-Python.svg?label=Stars&logo=github)](https://github.com/HXSecurity/DongTai-SDK-Python)
[![GitHub forks](https://img.shields.io/github/forks/HXSecurity/DongTai-SDK-Python?label=Forks&logo=github)](https://github.com/HXSecurity/DongTai-SDK-Python)
[![GitHub Contributors](https://img.shields.io/github/contributors/HXSecurity/DongTai-SDK-Python?label=Contributors&logo=github)](https://github.com/HXSecurity/DongTai-SDK-Python)


[![CI](https://github.com/HXSecurity/DongTai-SDK-Python/actions/workflows/release.yml/badge.svg)](https://github.com/HXSecurity/DongTai-SDK-Python/actions/workflows/release.yml)
[![Github Version](https://img.shields.io/github/v/release/HXSecurity/DongTai-SDK-Python?display_name=tag&include_prereleases&sort=semver)](https://github.com/HXSecurity/DongTai-SDK-Python/releases)
[![Release downloads](https://shields.io/github/downloads/HXSecurity/DongTai-SDK-Python/total)](https://github.com/HXSecurity/DongTai-SDK-Python/releases)


# Quick start

## You need a config file

config.json
```json
{
    "DongTai":{
        "token":"your token",
        "url":"http://127.0.0.1:90"
    }
}
```

## How to use:
```python
from dongtai_sdk.DongTai import DongTai
dongTaiSdk = DongTai("config.json")
```

## Support function (Continuous updating)
### Project
```python
GetProjectList(self,page,pageSize,name=None)
GetProjectVerList(self,projectId)
AddProjectVersion(self,projectId,verName,description,isEdit=True)
SearchProject(self,projectId)
```

### Agent
```python
DeleteAgent(self,agentId)
StartAgent(self,agentId)
StopAgent(self,agentId)
```
