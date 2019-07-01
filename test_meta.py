# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:33:31 2019

@author: Administrator
"""

from data.meta import DailyData
a = DailyData()
a.init()
b = a.GetBasicInfo()
a.AddMeta('open')