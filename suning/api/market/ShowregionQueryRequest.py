# -*- coding: utf-8 -*-

'''

Created on 2019-6-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShowregionQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryShowregion'

    def getApiMethod(self):

        return 'suning.market.showregion.query'



