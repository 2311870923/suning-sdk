#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-10-22

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SendgoodsModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.deliveryTime='发货时间'
a.expressCompanyCode='物流公司编码'
a.expressNo='运单号'
a.operateStyle='01'
a.productCode='物流公司名称'
a.sdcsOrderId='4454'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)