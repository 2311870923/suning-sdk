# -*- coding: utf-8 -*-

'''

Created on 2019-10-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class EnquirylistcallstateAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addEnquirylistcallstate'

    def getApiMethod(self):

        return 'suning.market.enquirylistcallstate.add'



