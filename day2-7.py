# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:20:56 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()

name=input("你的名字:")
message=input("你想說的話:")

mc.postToChat("["+name+"]"+message)