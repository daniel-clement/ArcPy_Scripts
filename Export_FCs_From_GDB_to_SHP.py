# This script was written by Daniel Clement - 2020
# Python 3 - ArcGIS Pro
"""
This script will convert all of the feature classes contained within the feature datasets of a geodatabase to shapefile.
"""

# do imports
import arcpy

# set parameters
#######################################################################################################################
# input geodatabase
inGDB = r"C:\data\example.gdb"

# output folder
outFolder = "C:\data\shapefiles"
#######################################################################################################################

# sets the workspace to the input geodatabase
arcpy.env.workspace = inGDB

# makes a list of the feature datasets in the geodatabase
datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

# loops through the feature datasets, each feature class therein, and converts each one to shapefile
for ds in datasets:

    # gets the feature classes in each feature dataset
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):

        # converts each feature class to a shape file
        arcpy.FeatureClassToShapefile_conversion(Input_Features=fc,
                                                 Output_Folder=outFolder)

        # prints the feature class which was converted
        print(fc + " --Exported Successfully")

print("\n#######################################################")
print("Successfully converted all Feature Classes to Shapefile")
print("#######################################################")
