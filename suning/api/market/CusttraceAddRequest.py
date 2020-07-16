# -*- coding: utf-8 -*-

'''

Created on 2019-3-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class CusttraceAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addCusttrace'

    def getApiMethod(self):

        return 'suning.market.custtrace.add'


