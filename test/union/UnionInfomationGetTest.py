#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-1-27

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.UnionInfomationGetRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("54fac3bb93475047e880ec3f04d81912", "8b349aa103fa1631c0118e7dff0940a8")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.goodsCode='000000000150003092'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)