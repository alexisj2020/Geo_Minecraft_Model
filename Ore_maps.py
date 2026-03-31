from PIL import Image
from PIL import ImageOps
import numpy as np
import sys

# Open ore maps
gold = Image.open("maps/gold_MODS.png")
gold = gold.convert('RGB')

iron = Image.open("maps/iron_mods.png")
iron = iron.convert('RGB')

copper = Image.open("maps/copper_mods.png")
copper = copper.convert('RGB')

beryl = Image.open("maps/beryl_mods.png")
beryl = beryl.convert('RGB')

coal = Image.open("maps/coal_mods.png")
coal = coal.convert('RGB')

# Resize smoothly down
gold_r = gold.resize((1153, 852), resample=Image.Resampling.NEAREST)

iron_r = iron.resize((1153, 852), resample=Image.Resampling.NEAREST)

copper_r = copper.resize((1153, 852), resample=Image.Resampling.NEAREST)

beryl_r = beryl.resize((1153, 852), resample=Image.Resampling.NEAREST)

coal_r = coal.resize((1153, 852), resample=Image.Resampling.NEAREST)

#create numpy array from resized map
gold_arr = np.array(gold_r)
gold_arr = gold_arr[:,:,:3]

iron_arr = np.array(iron_r)
iron_arr = iron_arr[:,:,:3]

copper_arr = np.array(copper_r)
copper_arr = copper_arr[:,:,:3]

beryl_arr = np.array(beryl_r)
beryl_arr = beryl_arr[:,:,:3]

coal_arr = np.array(coal_r)
coal_arr = coal_arr[:,:,:3]

#combine R, G, and B values into single rgb string
rows, cols, z = gold_arr.shape
gold_rgb = np.empty(shape=(rows,cols), dtype = int)
for x in range(rows):  
    for y in range(cols):
        gold_rgb[x,y] = ''.join(str(n) for n in gold_arr[x,y])

iron_rgb = np.empty(shape=(rows,cols), dtype = int)
for x in range(rows):  
    for y in range(cols):
        iron_rgb[x,y] = ''.join(str(n) for n in iron_arr[x,y])

copper_rgb = np.empty(shape=(rows,cols), dtype = int)
for x in range(rows):  
    for y in range(cols):
        copper_rgb[x,y] = ''.join(str(n) for n in copper_arr[x,y])

beryl_rgb = np.empty(shape=(rows,cols), dtype = int)
for x in range(rows):  
    for y in range(cols):
        beryl_rgb[x,y] = ''.join(str(n) for n in beryl_arr[x,y])

coal_rgb = np.empty(shape=(rows,cols), dtype = int)
for x in range(rows):  
    for y in range(cols):
        coal_rgb[x,y] = ''.join(str(n) for n in coal_arr[x,y])

np.savetxt('gold_rgb_arr.txt',gold_rgb)
np.savetxt('iron_rgb_arr.txt',iron_rgb)
np.savetxt('copper_rgb_arr.txt',copper_rgb)
np.savetxt('beryl_rgb_arr.txt',beryl_rgb)
np.savetxt('coal_rgb_arr.txt',coal_rgb)