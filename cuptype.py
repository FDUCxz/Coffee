# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:19:50 2020

@author: CXZ
"""

from beveragebase import Beverage 

class Midcup(Beverage):
    def __init__(self):
        super(Midcup, self).__init__()
        self.description = "中杯"
    def get_description(self):
        return self.description
    def cost(self):
        return 1.0
    
class Bigcup(Beverage):
    def __init__(self):
        super(Bigcup, self).__init__()
        self.description = "大杯"
    def get_description(self):
        return self.description
    def cost(self):
        return 2.0
    
class Superbigcup(Beverage):
    def __init__(self):
        super(Superbigcup, self).__init__()
        self.description = "超大杯"
    def get_description(self):
        return self.description
    def cost(self):
        return 3.0