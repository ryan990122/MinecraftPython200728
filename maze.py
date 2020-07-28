# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:07:42 2020

@author: user
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

mc.setBlocks(x+25,y-1,z+25,
             x-25,y-1,z-25,35)