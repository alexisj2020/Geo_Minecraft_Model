import numpy as np
import pandas as pd
import sys
from gdpc import __url__, Editor, Block
editor = Editor(buffering=True)

mag_grid = np.loadtxt('mag_grid.txt', delimiter=' ',dtype=float)

for x in range(0,200):
    for y in range(0,200):
        for z in range(150,151):
            if -1<mag_grid[y,x]<0:
                editor.placeBlock((x,z,y), Block("red_stained_glass"))
            if 0<mag_grid[y,x]<3:
                editor.placeBlock((x,z,y), Block("orange_stained_glass"))
            if 3<mag_grid[y,x]<6:
                editor.placeBlock((x,z,y), Block("yellow_stained_glass"))
            if 6<mag_grid[y,x]<9:
                editor.placeBlock((x,z,y), Block("lime_stained_glass"))
            if 9<mag_grid[y,x]<12:
                editor.placeBlock((x,z,y), Block("green_stained_glass"))
            if 12<mag_grid[y,x]<15:    
                editor.placeBlock((x,z,y), Block("cyan_stained_glass"))
            if 15<mag_grid[y,x]<18:
                editor.placeBlock((x,z,y), Block("light_blue_stained_glass"))
            if 18<mag_grid[y,x]<21:
                editor.placeBlock((x,z,y), Block("blue_stained_glass"))
            if 21<mag_grid[y,x]<24:
                editor.placeBlock((x,z,y), Block("purple_stained_glass"))
            if 24<mag_grid[y,x]<27:
                editor.placeBlock((x,z,y), Block("magenta_stained_glass"))
            if 27<mag_grid[y,x]:
                editor.placeBlock((x,z,y), Block("pink_stained_glass"))

for x in range(0,200):
    for y in range(0,200):
        for z in range(151,152):
            if -1<mag_grid[y,x]<0:
                editor.placeBlock((x,z,y), Block("red_carpet"))
            if 0<mag_grid[y,x]<3:
                editor.placeBlock((x,z,y), Block("orange_carpet"))
            if 3<mag_grid[y,x]<6:
                editor.placeBlock((x,z,y), Block("yellow_carpet"))
            if 6<mag_grid[y,x]<9:
                editor.placeBlock((x,z,y), Block("lime_carpet"))
            if 9<mag_grid[y,x]<12:
                editor.placeBlock((x,z,y), Block("green_carpet"))
            if 12<mag_grid[y,x]<15:    
                editor.placeBlock((x,z,y), Block("cyan_carpet"))
            if 15<mag_grid[y,x]<18:
                editor.placeBlock((x,z,y), Block("light_blue_carpet"))
            if 18<mag_grid[y,x]<21:
                editor.placeBlock((x,z,y), Block("blue_carpet"))
            if 21<mag_grid[y,x]<24:
                editor.placeBlock((x,z,y), Block("purple_carpet"))
            if 24<mag_grid[y,x]<27:
                editor.placeBlock((x,z,y), Block("magenta_carpet"))
            if 27<mag_grid[y,x]:
                editor.placeBlock((x,z,y), Block("pink_carpet"))