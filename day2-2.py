# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:21:33 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random


x,y,z=mc.player.getTilePos()

color=random.randrange(0,16)
mc.setBlocks(x+25,y-1,z+25,
             x-25,y-1,z-25,95,color)