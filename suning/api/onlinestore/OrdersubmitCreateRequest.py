# -*- coding: utf-8 -*-

'''

Created on 2020-3-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrdersubmitCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.platFormTrade = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'createOrdersubmit'

    def getApiMethod(self):

        return 'suning.onlinestore.ordersubmit.create'



