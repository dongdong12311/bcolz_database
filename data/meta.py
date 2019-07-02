# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:27:51 2019

@author: Administrator
"""
from abc import ABCMeta, abstractmethod, abstractproperty
import os
import bcolz
import numpy as np
class MetaData(metaclass=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def GetBasicInfo(self):
        pass
    
    @abstractmethod
    def AddMeta(self,meta):
        pass
    def _init(self,root_dir):
        if not os.path.exists(root_dir):            
            c = bcolz.carray(np.array(()),dtype='U16',
                             rootdir = root_dir )
            c.flush()        


class DailyData(MetaData):
    def __init__(self):
        root_dir = 'meta_of_daily_data'
        self._init(root_dir)
        self.__meta = bcolz.open(rootdir = root_dir)
        self.__meta.flush()
    
    def GetBasicInfo(self):
        return self.__meta
    def AddMeta(self,meta):
        if meta not in self.__meta:    
            self.__meta.append(meta)
    def __del__(self):
        self.__meta.flush()