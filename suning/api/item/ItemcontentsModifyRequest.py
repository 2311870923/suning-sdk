# -*- coding: utf-8 -*-'''Created on 2014-5-27, Auto Generated @author: momo'''from suning.api.abstract import AbstractApiclass ItemcontentsModifyRequest(AbstractApi):    '''    '''    def __init__(self):        AbstractApi.__init__(self)        self.productCode = None        self.saleSet = None        self.introduction = None        self.sellPoint = None        self.afterSaleServiceDec = None        self.freightTemplateId = None        self.childItem = None                self.itemCode = None                self.saleDate = None        self.sourceCountry = None                self.cmTitle = None                self.supplierImg1Url = None                self.supplierImg2Url = None                self.supplierImg3Url = None                self.supplierImg4Url = None                self.supplierImg5Url = None        self.supplierImg6Url = None                self.supplierImg7Url = None                self.supplierImg8Url = None                self.supplierImg9Url = None                self.supplierImg10Url = None        self.verticalPic = None                self.mobile = None        self.detailModule = None                self.mobileNew = None    def getApiBizName(self):        return 'itemContents'    def getApiMethod(self):        return 'suning.custom.itemcontents.modify'