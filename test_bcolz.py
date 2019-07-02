#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:32:01 2019

@author: dongdong
"""

import bcolz
import numpy as np
import sys
import os


from meta.meta import DailyData
import tushare as ts
ts.set_token('f867cf1c65e806c64096d26d7f7ea70db0c38bddb027c034f20c64de')
pro = ts.pro_api()    
def GetLatestStockList():
    data = pro.query('stock_basic', exchange='',
                     list_status='L',
                     fields='ts_code')
    return data['ts_code']
class LocalData:
    def __init__(self):
        self._meta_data = DailyData()
        self.__rootdir = 'daily_data'
        
    def GetData(self,meta,stock_code,start,end):
        pass
    def UpdateData(self):
        self.__UpdateStockList()
    
    def GetLocalStockList(self):
        return []
                    
    def __UpdateStockList(self):
        stock_list = GetLatestStockList()
        local_stock_list = self.GetLocalStockList()
        metas = self._meta_data.GetBasicInfo()
        for index,value in enumerate(metas):
            metas[index] = os.path.join(self.__rootdir,value)
            if  not os.path.exists(metas[index]):
                os.mkdir(metas[index])
        for stock in stock_list:
            if stock not in local_stock_list:
                for meta in metas:                    
                    self.__AddStock(meta,stock)        

    
    def __AddStock(self,meta,stock):
        'add a new stock if the stock code exists, return false'
        target_path = os.path.join(meta,stock)
        if os.path.exists(target_path):
            print(stock + " already_exists") 
            return False
        # create 
        c = bcolz.carray( np.array(()), rootdir=target_path)
        c.flush()
            
    def AddMeta(self,meta):
        self._meta_data.AddMeta(meta)
    
if __name__ == '__main__':
    a = LocalData()
    
    #a.AddMeta('open')
    a.UpdateData()


