# -*- coding: utf-8 -*-

'''

Created on 2019-3-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class MdsmgtDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'deleteMdsmgt'

    def getApiMethod(self):

        return 'suning.market.mdsmgt.delete'



