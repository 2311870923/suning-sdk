# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class LogisticcompanyGetRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.companyName = None

    def getApiBizName(self):
        return 'logisticCompany'

    def getApiMethod(self):
        return 'suning.custom.logisticcompany.get'

