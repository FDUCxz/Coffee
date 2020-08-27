# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 16:53:42 2020

@author: CXZ
"""
#饮料基类
class Beverage(object):
    description = "普通饮料"
    
    def get_description(self):
        return self.description
    
        
    def get_temperature(self, temperature):
        self.temperature = temperature
        return self.temperature
        
    def cost(self):
        pass
    
#调料类种类很多，故采用装饰者模式
#建立调料装饰者类
class CondimentDecorator(Beverage):
    def get_description(self):
        pass
    