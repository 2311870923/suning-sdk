# -*- coding: utf-8 -*-

'''

Created on 2019-7-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtylimitednumQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.cmmdtyList = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCmmdtylimitednum'

    def getApiMethod(self):

        return 'suning.retailer.cmmdtylimitednum.query'



