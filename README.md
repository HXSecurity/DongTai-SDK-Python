<!--
 * @Author: 饕餮
 * @Date: 2021-12-23 14:25:35
 * @version: 
 * @LastEditors: 饕餮
 * @LastEditTime: 2021-12-23 19:50:44
 * @Description: How to use
-->
# DongTai-SDK-Python
DongTai API SDK

1.your need a config file

config.json
{
    "DongTai":{
        "token":"your token",
        "url":"http://127.0.0.1:90"
    }
}

2.how to use:

from dongtai_sdk.DongTai import DongTai
dongTaiSdk = DongTai("config.json")