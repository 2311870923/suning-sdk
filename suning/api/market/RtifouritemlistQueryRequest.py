# -*- coding: utf-8 -*-

'''

Created on 2019-4-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class RtifouritemlistQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryRtifouritemlist'

    def getApiMethod(self):

        return 'suning.market.rtifouritemlist.query'



