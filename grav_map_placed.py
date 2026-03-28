import numpy as np
import pandas as pd
import sys
from gdpc import __url__, Editor, Block
editor = Editor(buffering=True)

grav_grid = np.loadtxt('grav_grid.txt', delimiter=' ',dtype=float)

for x in range(0,200):
    for y in range(0,200):
        for z in range(150,151):
            if 0<grav_grid[y,x]<25:
                editor.placeBlock((x,z,y), Block("red_stained_glass"))
            if 25<grav_grid[y,x]<50:
                editor.placeBlock((x,z,y), Block("orange_stained_glass"))
            if 50<grav_grid[y,x]<75:
                editor.placeBlock((x,z,y), Block("yellow_stained_glass"))
            if 75<grav_grid[y,x]<110:
                editor.placeBlock((x,z,y), Block("lime_stained_glass"))
            if 110<grav_grid[y,x]<150:
                editor.placeBlock((x,z,y), Block("green_stained_glass"))
            if 150<grav_grid[y,x]<200:    
                editor.placeBlock((x,z,y), Block("cyan_stained_glass"))
            if 200<grav_grid[y,x]<260:
                editor.placeBlock((x,z,y), Block("light_blue_stained_glass"))
            if 260<grav_grid[y,x]<330:
                editor.placeBlock((x,z,y), Block("blue_stained_glass"))
            if 330<grav_grid[y,x]<390:
                editor.placeBlock((x,z,y), Block("purple_stained_glass"))
            if 390<grav_grid[y,x]<460:
                editor.placeBlock((x,z,y), Block("magenta_stained_glass"))
            if 460<grav_grid[y,x]:
                editor.placeBlock((x,z,y), Block("pink_stained_glass"))

for x in range(0,200):
    for y in range(0,200):
        for z in range(151,152):
            if 0<grav_grid[y,x]<25:
                editor.placeBlock((x,z,y), Block("red_carpet"))
            if 25<grav_grid[y,x]<50:
                editor.placeBlock((x,z,y), Block("orange_carpet"))
            if 50<grav_grid[y,x]<75:
                editor.placeBlock((x,z,y), Block("yellow_carpet"))
            if 75<grav_grid[y,x]<110:
                editor.placeBlock((x,z,y), Block("lime_carpet"))
            if 110<grav_grid[y,x]<150:
                editor.placeBlock((x,z,y), Block("green_carpet"))
            if 150<grav_grid[y,x]<200:    
                editor.placeBlock((x,z,y), Block("cyan_carpet"))
            if 200<grav_grid[y,x]<260:
                editor.placeBlock((x,z,y), Block("light_blue_carpet"))
            if 260<grav_grid[y,x]<330:
                editor.placeBlock((x,z,y), Block("blue_carpet"))
            if 330<grav_grid[y,x]<390:
                editor.placeBlock((x,z,y), Block("purple_carpet"))
            if 390<grav_grid[y,x]<460:
                editor.placeBlock((x,z,y), Block("magenta_carpet"))
            if 460<grav_grid[y,x]:
                editor.placeBlock((x,z,y), Block("pink_carpet"))