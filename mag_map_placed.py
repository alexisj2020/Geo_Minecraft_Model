import numpy as np
import pandas as pd
import sys
from gdpc import __url__, Editor, Block
editor = Editor(buffering=True)

#load in magnetic data
mag_grid = np.loadtxt('mag_data_2.txt', delimiter=' ',dtype=float)

#place glass blocks in sky of minecraft world above play area
#colours correspond to gravity data values
#the distribution of colours will depend on the data range
for x in range(0,200):
    for y in range(0,200):
        for z in range(100,101):
            if -1<mag_grid[x,y]<=2:
                editor.placeBlock((x,z,y), Block("red_stained_glass"))
            if 2<mag_grid[x,y]<=4:
                editor.placeBlock((x,z,y), Block("orange_stained_glass"))
            if 4<mag_grid[x,y]<=6:
                editor.placeBlock((x,z,y), Block("yellow_stained_glass"))
            if 6<mag_grid[x,y]<=8:
                editor.placeBlock((x,z,y), Block("lime_stained_glass"))
            if 8<mag_grid[x,y]<=10:
                editor.placeBlock((x,z,y), Block("green_stained_glass"))
            if 10<mag_grid[x,y]<=12:    
                editor.placeBlock((x,z,y), Block("cyan_stained_glass"))
            if 12<mag_grid[x,y]<=14:
                editor.placeBlock((x,z,y), Block("light_blue_stained_glass"))
            if 14<mag_grid[x,y]<=16:
                editor.placeBlock((x,z,y), Block("blue_stained_glass"))
            if 16<mag_grid[x,y]<=18:
                editor.placeBlock((x,z,y), Block("purple_stained_glass"))
            if 18<mag_grid[x,y]<=20:
                editor.placeBlock((x,z,y), Block("magenta_stained_glass"))
            if 20<mag_grid[x,y]:
                editor.placeBlock((x,z,y), Block("pink_stained_glass"))

#placing carpet above the glass blocks using the same colour scheme
#using both glass and carpet results in best appearance
for x in range(0,200):
    for y in range(0,200):
        for z in range(101,102):
            if -1<mag_grid[x,y]<=2:
                editor.placeBlock((x,z,y), Block("red_carpet"))
            if 2<mag_grid[x,y]<=4:
                editor.placeBlock((x,z,y), Block("orange_carpet"))
            if 4<mag_grid[x,y]<=6:
                editor.placeBlock((x,z,y), Block("yellow_carpet"))
            if 6<mag_grid[x,y]<=8:
                editor.placeBlock((x,z,y), Block("lime_carpet"))
            if 8<mag_grid[x,y]<=10:
                editor.placeBlock((x,z,y), Block("green_carpet"))
            if 10<mag_grid[x,y]<=12:    
                editor.placeBlock((x,z,y), Block("cyan_carpet"))
            if 12<mag_grid[x,y]<=14:
                editor.placeBlock((x,z,y), Block("light_blue_carpet"))
            if 14<mag_grid[x,y]<=16:
                editor.placeBlock((x,z,y), Block("blue_carpet"))
            if 16<mag_grid[x,y]<=18:
                editor.placeBlock((x,z,y), Block("purple_carpet"))
            if 18<mag_grid[x,y]<=20:
                editor.placeBlock((x,z,y), Block("magenta_carpet"))
            if 20<mag_grid[x,y]:
                editor.placeBlock((x,z,y), Block("pink_carpet"))