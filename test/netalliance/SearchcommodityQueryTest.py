#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-5-15

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SearchcommodityQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.branch='1'
a.cityCode='025'
a.coupon='1'
a.couponMark='1'
a.endPrice='20.00'
a.keyword='手机'
a.pageIndex='1'
a.pgSearch='1'
a.picHeight='200'
a.picWidth='200'
a.saleCategoryCode='50000'
a.size='10'
a.snfwservice='1'
a.snhwg='1'
a.sortType='1'
a.startPrice='10.00'
a.suningService='1'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)