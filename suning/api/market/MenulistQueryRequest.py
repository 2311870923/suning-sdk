# -*- coding: utf-8 -*-

'''

Created on 2020-2-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class MenulistQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryMenulist'

    def getApiMethod(self):

        return 'suning.market.menulist.query'



