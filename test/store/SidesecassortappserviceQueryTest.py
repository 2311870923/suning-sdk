#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-3-21

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SidesecassortappserviceQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appStoreCode='S03006330(商户自定义编码和平台自定义编码必传一个)'
a.protypeid='10000023'
a.storeCode='S03006330(商户自定义编码和平台自定义编码必传一个)'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)