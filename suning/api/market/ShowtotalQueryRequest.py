# -*- coding: utf-8 -*-

'''

Created on 2019-6-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShowtotalQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryShowtotal'

    def getApiMethod(self):

        return 'suning.market.showtotal.query'



