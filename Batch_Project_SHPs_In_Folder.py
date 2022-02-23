# This script was developed by Daniel Clement - 2020
# Python 3 - ArcGIS Pro
"""
This script will project all of the shapefiles in the input folder to the chosen projection
"""

import os
import arcpy
from glob import glob

# Set Parameters
#######################################################################################################################
# folder with the shapefiles you want to project
inFolder = r"C:\data\shapefiles"

# folder you want the projected shapefiles to be output to
outFolder = r"C:\data\shapefiles_projected"

# the EPSG code of the output coordinate system you want the aster to be projected into - https://epsg.io/
projection = 4326
#######################################################################################################################

# make a list of all the shapefiles in the input folder
shp_list = glob(inFolder + "/*.shp")

# set the chosen projection as an arc spatial reference object
sr = arcpy.SpatialReference(projection)

# for each shapefile in the shp_list, project it to the chosen projection
for shp in shp_list:

    # get the name of the input shapefile
    basename2 = os.path.basename(shp)

    # create the output file name
    outFile = os.path.join(outFolder, "{}_PRJ.shp".format(basename2.split('.')[0]))

    # use arcpy to project the shapefile
    arcpy.Project_management(in_dataset=shp,
                             out_dataset=outFile,
                             out_coor_system=sr)

    # print the file which was projected
    (file, ext) = os.path.splitext(basename2)
    print(file + ext + " -- Projected Successfully!")

print("\n######################################")
print("Successfully projected all SHP files")
print("######################################")


