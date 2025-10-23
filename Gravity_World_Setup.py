import numpy as np
from numpy import random
import pandas as pd
import sys

from gdpc import __url__, Editor, Block

editor = Editor(buffering=True)
#buildArea = editor.getBuildArea()
#editor.loadWorldSlice(cache=True)
#heightmap = editor.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"]

#add fence around game area
peri = list(range(-1,258))
for x in peri:
    editor.placeBlock((-1, 1, x), Block("dark_oak_fence"))
    editor.placeBlock((257, 1, x), Block("dark_oak_fence"))
    editor.placeBlock((x, 1, -1), Block("dark_oak_fence"))
    editor.placeBlock((x, 1, 257), Block("dark_oak_fence"))

y_dirt = list(range(-5,0))
y_stone = list(range(-64,-5))

#create a simple subsurface
for x in range(0,256):
    for z in range(0,256):
        editor.placeBlock((x,0,z), Block("grass_block"))

for x in range(0,256):
    for z in range(0,256):
        for y in y_dirt:
            editor.placeBlock((x,y,z), Block("dirt"))

for x in range(0,256):
    for z in range(0,256):
        for y in y_stone:
            editor.placeBlock((x,y,z), Block("stone"))

#create random distributions of ore bodies within a 10 cubic metre range
iron_ore = random.choice([1, 2], p=[0.2, 0.8], size=(10, 10, 10))
gold_ore = random.choice([1, 3], p=[0.2, 0.8], size=(10, 10, 10))
diamond_ore = random.choice([1, 4], p=[0.25, 0.75], size=(10, 10, 10))

#create a 3D array of random integers within study coordinates
x_rand = np.random.randint(0, 246 + 1, size=18).tolist()
z_rand = np.random.randint(0, 246 + 1, size=18).tolist()
y_rand = np.random.randint(-64, -10 + 1, size=18).tolist()

coords_rand = np.dstack((x_rand, z_rand, y_rand))

#use random coordinates to randomly space ore bodies and place these blocks at these coordinates in minecraft
for x in range(0,10):
    for y in range(0,10):
        for z in range(0,10):
            for i in range(0,9):
                if iron_ore[x,y,z] == 2:
                    editor.placeBlock((x+coords_rand[0,i,0],y+coords_rand[0,i,2],z+coords_rand[0,i,1]), Block("iron_ore"))

for x in range(0,10):
    for y in range(0,10):
        for z in range(0,10):
            for i in range(9,15):
                if gold_ore[x,y,z] == 3:
                    editor.placeBlock((x+coords_rand[0,i,0],y+coords_rand[0,i,2],z+coords_rand[0,i,1]), Block("gold_ore"))

for x in range(0,10):
    for y in range(0,10):
        for z in range(0,10):
            for i in range(15,18):
                if diamond_ore[x,y,z] == 4:
                    editor.placeBlock((x+coords_rand[0,i,0],y+coords_rand[0,i,2],z+coords_rand[0,i,1]), Block("diamond_ore"))