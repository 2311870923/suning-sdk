# -*- coding: utf-8 -*-

'''

Created on 2019-8-1

@author: suning

'''

from suning.api.abstract import AbstractApi



class PcitiesQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPcities'

    def getApiMethod(self):

        return 'suning.market.pcities.query'



