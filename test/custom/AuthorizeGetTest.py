#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-4-13

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.AuthorizeGetRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.accessKeyId='123456324'
a.accessSign='ca614d6d8289ec263462d64d5e465930'
a.name='苏宁'
a.redirectUrl='http://your.web.site'
a.timeStamp='1584429071000'
a.userId='1232482235'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)