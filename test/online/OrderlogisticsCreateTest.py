#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-11-15

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderlogisticsCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.expressCompanyName='顺丰'
a.expressOrderId='343559087343'
a.logisticsCode='001'
a.operateType='01：退货'
a.orderId='2019111101'
a.orderItemId='2019111101001'
a.reOrderItemId='R20191111001001'
a.sheetId='001'
a.skuId='000000000002349001'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)