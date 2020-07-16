# -*- coding: utf-8 -*-

'''

Created on 2020-2-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class HometargetsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryHometargets'

    def getApiMethod(self):

        return 'suning.market.hometargets.query'



