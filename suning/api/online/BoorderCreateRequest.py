# -*- coding: utf-8 -*-

'''

Created on 2019-12-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class BoorderCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.platFormTrade = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'createBoorder'

    def getApiMethod(self):

        return 'suning.online.boorder.create'



