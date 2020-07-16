# -*- coding: utf-8 -*-

'''

Created on 2020-7-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class FreighttemplatenewUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.commonMap = None
        self.specialList = None
        self.vendorCode = None
        
        self.setParamRule({
        	'vendorCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updateFreighttemplatenew'

    def getApiMethod(self):

        return 'suning.custom.freighttemplatenew.update'



