# This script was written by Daniel Clement - 2022
# Python-3
"""
This script will loop through the CSV's within a folder, that consist of a number of lat/long coordinates,
and converts them to a polygon shapefile.
"""
# Uses the ArcGIS Pro python interpreter

# do imports
import os
import arcpy
from glob import glob

# set parameters
#######################################################################################################################
# input folder
inDir = r"c:\data\csv"
#######################################################################################################################


# gets list of csv's in input folder
csvList = glob(inDir + "/*.csv")

for csv in csvList:
    ####################
    # convert to point
    ####################
    # gets the name of the csv - without the path attached
    inCsvName = os.path.basename(csv)

    # replaces the '.csv' in the name with 'point.csv'
    outPointName = inCsvName.replace(".csv", "_Point.shp")

    # replaces the new name with the original csv path
    outPointShp = csv.replace(inCsvName, outPointName)

    # field with x coords
    xFieldName = "Long"
    # field with y coords
    yFieldName = "Lat"

    # convert the xy csv to points
    arcpy.management.XYTableToPoint(in_table=csv,
                                    out_feature_class=outPointShp,
                                    x_field=xFieldName,
                                    y_field=yFieldName,
                                    coordinate_system=arcpy.SpatialReference(4326)
                                    )

    #####################
    # convert to polyline
    #####################
    # replaces the '.csv' in the name with 'point.csv'
    outPolylineName = inCsvName.replace(".csv", "_Polyline.shp")

    # replaces the new name with the original csv path
    outPolylineShp = csv.replace(inCsvName, outPolylineName)

    arcpy.PointsToLine_management(input_features=outPointShp,
                                  Output_Feature_Class=outPolylineShp,
                                  Close_Line="CLOSE")

    ####################
    # convert to polygon
    ####################
    # replaces the '.csv' in the name with 'point.csv'
    outPolygonName = inCsvName.replace(".csv", "_Polygon.shp")

    # replaces the new name with the original csv path
    outPolygonShp = csv.replace(inCsvName, outPolygonName)

    # convert the polylines to polygon
    arcpy.FeatureToPolygon_management(in_features=outPolylineShp,
                                      out_feature_class=outPolygonShp
                                      )

print("\nProcess complete!")