# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:46:50 2020

@author: CXZ
"""

from beveragebase import CondimentDecorator, Beverage

class Yuanwei(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
        
    def get_description(self):
        return self.beverage.get_description()+",原味糖浆"
    def cost(self):
        return 0.5 + self.beverage.cost()
    
    
class Xiangcao(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
        
    def get_description(self):
        return self.beverage.get_description()+",香草糖浆"
    def cost(self):
        return 0.6 + self.beverage.cost()
    
class Jiaotang(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
        
    def get_description(self):
        return self.beverage.get_description()+",焦糖糖浆"
    def cost(self):
        return 0.7 + self.beverage.cost()
    
class Zhenguo(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
        
    def get_description(self):
        return self.beverage.get_description()+",榛果糖浆"
    def cost(self):
        return 1.0 + self.beverage.cost()
    
class Moka(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
        
    def get_description(self):
        return self.beverage.get_description()+",摩卡糖浆"
    def cost(self):
        return 0.8 + self.beverage.cost()
    