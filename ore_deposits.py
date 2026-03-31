import numpy as np
import sys
from gdpc import __url__, Editor, Block, Rect
editor = Editor(buffering=True)

print("What x line would you like to add?:")
xs = sys.argv[1]
x=int(xs)
print("Please add line "+str(x))

rect = Rect((x,0), ((x+1),853))

worldSlice = editor.loadWorldSlice(rect)
heightmap = worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"]

gold_rgb = np.loadtxt("gold_rgb_arr.txt").astype(np.int64)
iron_rgb = np.loadtxt("iron_rgb_arr.txt").astype(np.int64)
copper_rgb = np.loadtxt("copper_rgb_arr.txt").astype(np.int64)
beryl_rgb = np.loadtxt("beryl_rgb_arr.txt").astype(np.int64)
coal_rgb = np.loadtxt("coal_rgb_arr.txt").astype(np.int64)

#placing blocks in minecraft according to mineral occurrences
for z in range(0,852):
    if gold_rgb[z,x]!=255255255:
        x_g = np.full(10,x)
        z_g = np.full(10,z)
        ypg = np.random.choice(np.arange((heightmap[0,z]-20),heightmap[0,z]),size=10, p=[0.05, 0.05, 0.05, 0.05, 0.05,
                                                                                         0.055, 0.055, 0.055, 0.055, 0.055, 
                                                                                         0.055, 0.05, 0.05, 0.05, 0.05, 
                                                                                         0.05, 0.05, 0.05, 0.05, 0.02])
        coords_g = np.vstack((x_g, ypg, z_g)).T
        editor.placeBlock((coords_g), Block("gold_ore"))

for z in range(0,852):
    if iron_rgb[z,x]!=255255255:
        x_i = np.full(10,x)
        z_i = np.full(10,z)
        ypi = np.random.choice(np.arange((heightmap[0,z]-20),heightmap[0,z]),size=10, p=[0.05, 0.05, 0.05, 0.05, 0.05,
                                                                                         0.055, 0.055, 0.055, 0.055, 0.055, 
                                                                                         0.055, 0.05, 0.05, 0.05, 0.05, 
                                                                                         0.05, 0.05, 0.05, 0.05, 0.02])
        coords_i = np.vstack((x_i, ypi, z_i)).T
        editor.placeBlock((coords_i), Block("iron_ore"))

for z in range(0,852):
    if copper_rgb[z,x]!=255255255:
        x_cp = np.full(10,x)
        z_cp = np.full(10,z)
        ypcp = np.random.choice(np.arange((heightmap[0,z]-20),heightmap[0,z]),size=10, p=[0.05, 0.05, 0.05, 0.05, 0.05,
                                                                                         0.055, 0.055, 0.055, 0.055, 0.055, 
                                                                                         0.055, 0.05, 0.05, 0.05, 0.05, 
                                                                                         0.05, 0.05, 0.05, 0.05, 0.02])
        coords_cp = np.vstack((x_cp, ypcp, z_cp)).T
        editor.placeBlock(coords_cp, Block("copper_ore"))

for z in range(0,852):
    if beryl_rgb[z,x]!=255255255:
        x_b = np.full(10,x)
        z_b = np.full(10,z)
        ypb = np.random.choice(np.arange((heightmap[0,z]-20),heightmap[0,z]),size=10, p=[0.05, 0.05, 0.05, 0.05, 0.05,
                                                                                         0.055, 0.055, 0.055, 0.055, 0.055, 
                                                                                         0.055, 0.05, 0.05, 0.05, 0.05, 
                                                                                         0.05, 0.05, 0.05, 0.05, 0.02])
        coords_b = np.vstack((x_b, ypb, z_b)).T
        editor.placeBlock((coords_b), Block("emerald_ore"))

for z in range(0,852):
    if coal_rgb[z,x]!=255255255:
        x_c = np.full(10,x)
        z_c = np.full(10,z)
        ypc = np.random.choice(np.arange((heightmap[0,z]-20),heightmap[0,z]),size=10, p=[0.05, 0.05, 0.05, 0.05, 0.05,
                                                                                         0.055, 0.055, 0.055, 0.055, 0.055, 
                                                                                         0.055, 0.05, 0.05, 0.05, 0.05, 
                                                                                         0.05, 0.05, 0.05, 0.05, 0.02])
        coords_c = np.vstack((x_c, ypc, z_c)).T
        editor.placeBlock((coords_c), Block("coal_ore"))

print("Ore added for x line " + str(x))