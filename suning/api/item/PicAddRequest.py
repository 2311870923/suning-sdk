# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class PicAddRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)

    def getApiBizName(self):
        return 'pic'

    def getApiMethod(self):
        return 'suning.custom.pic.add'
