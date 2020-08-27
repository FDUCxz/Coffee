# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:36:30 2020

@author: CXZ
"""

from beveragebase import CondimentDecorator


class Quanzhi(CondimentDecorator):
    def __init__(self, beverage):
        self.description = "全脂"
        self.beverage = beverage
        
    def get_description(self):
        return self.description
    
    def cost(self):
        return 1.0 + self.beverage.cost()
    
class Yanmai(CondimentDecorator):
    def __init__(self, beverage):
        self.description = "燕麦"
        self.beverage = beverage
        
    def get_description(self):
        return self.description
    
    def cost(self):
        return 2.0 + self.beverage.cost()
    
class Tuozhi(CondimentDecorator):
    def __init__(self, beverage):
        self.description = "脱脂"
        self.beverage = beverage
        
    def get_description(self):
        return self.description
    
    def cost(self):
        return 3.0 + self.beverage.cost()