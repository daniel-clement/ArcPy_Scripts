# This script was developed by Daniel Clement - 2020
# Python 3 - ArcGIS Pro
"""
This script will clip the shapefiles in the in folder to the extent of the clip feature.
"""

# do imports
import os
import arcpy
from glob import glob

# Set Parameters
#######################################################################################################################
# Folder of SHP files to be clipped
inFolder = r"c:\data\shapefiles"

# Folder where you want the clipped SHPs to go
outFolder = r"c:\data\shapefiles_clipped"

# SHP file you want to clip the other SHPs with
clipFeat = r"c:\data\aoi_extent.shp"
#######################################################################################################################

# get a list of all the shapefiles in the input folder
shp_list = glob(inFolder + "/*.shp")

# loop through the shp files in the shp_list and clip them to the extent of the clipFeat
for shp in shp_list:

    # get the name of the input shapefile
    basename2 = os.path.basename(shp)

    # create the output shp file name
    outFile = os.path.join(outFolder, "{}_Clip.shp".format(basename2.split('.')[0]))

    # utilize arcpy to clip the input shapefile to the extent of the clipFeat
    arcpy.Clip_analysis(in_features=shp,
                        clip_features=clipFeat,
                        out_feature_class=outFile)

    # print the file which was clipped
    (file, ext) = os.path.splitext(basename2)
    print(file + ext + " -- Clipped Successfully!")

print("\n######################################")
print("Successfully clipped all SHP files")
print("######################################")
