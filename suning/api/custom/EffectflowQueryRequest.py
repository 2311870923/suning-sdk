# -*- coding: utf-8 -*-

'''

Created on 2020-6-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class EffectflowQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        self.pageNo = None
        self.pageSize = None
        self.taskId = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryEffectflow'

    def getApiMethod(self):

        return 'suning.custom.effectflow.query'



