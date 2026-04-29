# Making a geologic map of Newfoundland in Minecraft
Building the Newfoundland map involves multiple steps, some involving other programs that you will
need if you want to try building your own maps. These programs include WorldPainter, which is used to generate
Minecraft worlds from elevation maps, and QGIS, which is used to make elevation and geologic maps from available
data. Both of these applications are free to use.

The first step in building this map is finding the necessary data. .dbf files are obtained from freely available
resources online. The geologic data is acquired from the GeoAtlas NL website, and the elevation data is acquired
from the Department of Forestry, Agriculture, and Lands GeoHub of NL website. These data are imported in QGIS to
make maps of these data. Both maps are saved as PNGs, making sure that the lateral extent and resolution of both maps
is the exact same.

The base Minecraft world is made in WorldPainter. To do this, open WorldPainter and import the elevation map by going 
to File -> Import new World -> From height map. Here we decide what the size of the map will be. For the NL map, 
we set the size to 20% of the original size of the image, which comes out to 1153 x 852 blocks in Minecraft. The
height mapping values should also be changed to make sure the elevation isn't overly exaggerated. Under the
"To Minecraft" section, we set "Low mapping" to 0, "Water level" to 0, and "High mapping" to 40 (this may take some
iteration to decide what looks best). Then, we click OK to generate the world. We can click View -> Show 3D view to
see what the world looks like. If the elevation looks too high or low, try importing the map again and change the
mapping values. To generate the Minecraft world, go to File -> Export -> Export as new Minecraft map. Then, we make
a few final adjustments. Here, select the desired world mode (survival or creative) and whether to allow cheats
and structures. Also, set the centre of the world. We want the corner of the map to be at (0,0), so set the centre
of the world as the centre of the map (half the coordinates set when importing the height map). Also, go to the
surface tab and select your desired border type (I recommend void or water, I chose void for the NL map). Now we save
this map as a Minecraft world, making sure to save it in the appropriate saves folder of the Minecraft app. If you
would like more info on how to use WorldPainter, check out this tutorial I found which taught me everything I know
https://www.youtube.com/watch?v=E1cPiqghlys&list=LL&index=19.

Now we want to set up a legend for the geology, where we map each of the rock types in the geologic map to a Minecraft
block type.

Now we move on to using the codes included in this repo. We can write code to edit Minecraft worlds. Make sure you
have the right setup by going to the Code to Minecraft Tutorial first.

The first thing we've done is add water to the ocean of the map. You can skip this step if the area you're modelling
doesn't have any ocean. To do this, open the Minecraft world you've made, and run the "add_water.py" file. This code
detects all areas where the height of the ground in the Minecraft world is at 0 elevation, and then replaces the top
block with air, and the block below with water. This puts an "ocean" around the island.
