# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class ParallelinventoryModifyRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.productCode = None
        self.itemCode = None
        self.destInvNum = None
        self.invCode = None                self.invType = None
    def getApiBizName(self):
        return 'parallelInventory'

    def getApiMethod(self):
        return 'suning.custom.parallelinventory.modify'

