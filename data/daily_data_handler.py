# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:02:33 2019

@author: Administrator
"""
import bcolz
import os
from .meta import DailyData
from trading_dates_handler import ThisYear
class SliceData:
    def __init__(self):
        pass

class DailyDataHandler:
    def __init__(self):
        pass
    def Update(self):
        "更新所有的数据"
        pass
    
    def GetSliceData(self,N = 1):
        return SliceData()
    
    def GetData(self,stock_code,field,N = 1):
    
        return 0.0
class DataUpdator:    
    def __init__(self):
        pass
    def Update(self):
        pass
class DailyDataUpdator:
    def __init__(self):
        self.__rootdir = "daily_stock_data"
        "股票数据的最小存储单位是年"
        self._data = None
    def init(self,meta):
        try:
            self._data = bcolz.open(os.path.join(self.__rootdir,meta))
        except:
            raise "I can't find the data"
            
    def Update(self):
        self._Update()        
    def _Update(self):
        "更新单元内的股票代码"
        fields = self.GetDailyStockFields()
        for field in fields:
            self._UpdateStockCode(field)
            self._UpdateStocks(field)
    def _UpdateStockCode(self,field):
        codes = GetLatestCode(self.meta)
        dic = data.attrs['line_map']
        for code in dic.keys():
            if code not in codes:
                dic.update({code:[]})

    def _UpdateStocks(self,field):
        if data.attrs['locked'] == True:
            raise "Data had beend locked！！"
        "ok I need to Update data but I don't know how to realize it "
        "ok it seems that I did not do accomplish anything "
        
        
        
        
        
    