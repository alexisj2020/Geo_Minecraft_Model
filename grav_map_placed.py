import numpy as np
import pandas as pd
import sys
from gdpc import __url__, Editor, Block
editor = Editor(buffering=True)

#load in gravity data
grav_grid = np.loadtxt('grav_grid.txt', delimiter=' ',dtype=float)

#place glass blocks in sky of minecraft world above play area
#colours correspond to gravity data values
#the distribution of colours will depend on the data range
for x in range(0,200):
    for y in range(0,200):
        for z in range(100,101):
            if 0<grav_grid[y,x]<=50:
                editor.placeBlock((x,z,y), Block("red_stained_glass"))
            if 50<grav_grid[y,x]<=100:
                editor.placeBlock((x,z,y), Block("orange_stained_glass"))
            if 100<grav_grid[y,x]<=150:
                editor.placeBlock((x,z,y), Block("yellow_stained_glass"))
            if 150<grav_grid[y,x]<=200:
                editor.placeBlock((x,z,y), Block("lime_stained_glass"))
            if 200<grav_grid[y,x]<=250:
                editor.placeBlock((x,z,y), Block("green_stained_glass"))
            if 250<grav_grid[y,x]<=300:    
                editor.placeBlock((x,z,y), Block("cyan_stained_glass"))
            if 300<grav_grid[y,x]<=400:
                editor.placeBlock((x,z,y), Block("light_blue_stained_glass"))
            if 400<grav_grid[y,x]<=500:
                editor.placeBlock((x,z,y), Block("blue_stained_glass"))
            if 500<grav_grid[y,x]<=600:
                editor.placeBlock((x,z,y), Block("purple_stained_glass"))
            if 600<grav_grid[y,x]<=700:
                editor.placeBlock((x,z,y), Block("magenta_stained_glass"))
            if 700<grav_grid[y,x]:
                editor.placeBlock((x,z,y), Block("pink_stained_glass"))


#placing carpet above the glass blocks using the same colour scheme
#using both glass and carpet results in best appearance
for x in range(0,200):
    for y in range(0,200):
        for z in range(101,102):
            if 0<grav_grid[y,x]<=50:
                editor.placeBlock((x,z,y), Block("red_carpet"))
            if 50<grav_grid[y,x]<=100:
                editor.placeBlock((x,z,y), Block("orange_carpet"))
            if 100<grav_grid[y,x]<=150:
                editor.placeBlock((x,z,y), Block("yellow_carpet"))
            if 150<grav_grid[y,x]<=200:
                editor.placeBlock((x,z,y), Block("lime_carpet"))
            if 200<grav_grid[y,x]<=250:
                editor.placeBlock((x,z,y), Block("green_carpet"))
            if 250<grav_grid[y,x]<=300:    
                editor.placeBlock((x,z,y), Block("cyan_carpet"))
            if 300<grav_grid[y,x]<=400:
                editor.placeBlock((x,z,y), Block("light_blue_carpet"))
            if 400<grav_grid[y,x]<=500:
                editor.placeBlock((x,z,y), Block("blue_carpet"))
            if 500<grav_grid[y,x]<=600:
                editor.placeBlock((x,z,y), Block("purple_carpet"))
            if 600<grav_grid[y,x]<=700:
                editor.placeBlock((x,z,y), Block("magenta_carpet"))
            if 700<grav_grid[y,x]:
                editor.placeBlock((x,z,y), Block("pink_carpet"))