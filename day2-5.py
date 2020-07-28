# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:13:31 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
     x,y,z=mc.player.getTilePos()
     
     a=mc.getBlock(x,y-1,z+1)
     b=mc.getBlock(x,y-1,z-1)
     c=mc.getBlock(x+1,y-1,z)
     d=mc.getBlock(x-1,y-1,z)
     
     if a==9 or b==9\
     or c==9or d==9:
         mc.setBlocks(x-1,y-1,z-1,
                      x+1,y-1,z+1,79)