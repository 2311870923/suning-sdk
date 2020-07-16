# -*- coding: utf-8 -*-

'''

Created on 2020-2-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class LinkboardlossQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryLinkboardloss'

    def getApiMethod(self):

        return 'suning.market.linkboardloss.query'



