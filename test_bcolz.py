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
rootdir = "data"
data_path = "20180101"
target_path = os.path.join(rootdir,data_path)

# create a c table
data = bcolz.zeros(0, dtype={'names':['open','high','low','close'],
                             'formats':["f8","f8","f8","f8"]}, rootdir=target_path,mode = 'r')
data.cols

class LocalData:
    def __init__(self):
        pass
    def GetData(self,index,stock_code,start,end):
        pass
    
    def AddIndex(self,index):
        'add a new stock index'
        pass
    
    def AddStock(self,index,stock):
        'add a new stock if the stock code exists, return false'
        pass
    
    def UpdateStock(self,index,stock_code,data,calendar):
        pass
    



