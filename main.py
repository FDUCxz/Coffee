# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:58:49 2020

@author: CXZ
"""

from beveragebase import Beverage, CondimentDecorator
from cuptype import Midcup, Bigcup, Superbigcup
from milktype import Quanzhi, Yanmai, Tuozhi
from condimentdecorator import *

if __name__ == "__main__":
    
    cuptypes = {"中杯":Midcup(), "大杯":Bigcup(), "超大杯":Superbigcup()}
    milktypes = {"全脂":Quanzhi, "燕麦":Yanmai, "脱脂":Tuozhi}
    condimenttypes = {"原味糖浆": Yuanwei,"香草糖浆":Xiangcao, "焦糖糖浆":Jiaotang, "榛果糖浆":Zhenguo, "摩卡糖浆":Moka }
    
    try:
        print("欢迎来到咖啡店！请选购咖啡！")
        cuptype = input("请输入杯型（中杯/大杯/超大杯）:")          
        coffee = cuptypes[cuptype]
        temperature = input("请输入温度（冰/常温/热）：")
        coffee.get_temperature(temperature)
        milktype = input("请输入牛奶类型（全脂/燕麦/脱脂）:")
        coffee = milktypes[milktype](coffee)
        key = None
        while key not in ["N","n"]:            
            condimenttype = input("情输入加入的酱料（原味糖浆/香草糖浆/焦糖糖浆/榛果糖浆/摩卡糖浆）：")
            coffee = condimenttypes[condimenttype](coffee)
            key = input("还需要添加酱料吗[Y/N]")
        print("购买商品为：" + temperature + coffee.get_description() + "咖啡一杯"+ "￥"+str(coffee.cost()))
    except Exception as e:
        print("输入有误，请重新输入！")
    finally:
        print("欢迎下次光临!")

    
    
    
    