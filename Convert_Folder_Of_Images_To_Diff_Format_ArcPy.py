# This script was written by Daniel Clement - 2020
# This script will take a folder of images, and convert them to a different image format.
# Python 3 - ArcGIS Pro

# do imports
import os
import arcpy
from glob import glob

# set parameters
############################################
# folder containing images you want to convert
# acceptable input formats: ".bil", ".bip", ".bmp", ".bsq", ".dat", ".gif", ".img", ".jpg", ".jp2", ".png", ".tif"
inFolder = r"C:\data\images"

# folder where the converted images will be output to
outFolder = r"C:\data\images_converted"

# the format you want the images to be converted to
# acceptable output formats: ".bil", ".bip", ".bmp", ".bsq", ".dat", ".gif", ".img", ".jpg", ".jp2", ".png", ".tif"
outFormat_ext = ".tif"
############################################


#################################################
# Step 1 - Determine image format of input images
#################################################
# get the first entry in a list of the input files
inFiles = os.listdir(inFolder)[0]

# get the file extention of the first input file
inFormat_ext = os.path.splitext(inFiles)[1]

# make a list of the acceptable file formats
goodFormats = [".bil", ".bip", ".bmp", ".bsq", ".dat", ".gif", ".img", ".jpg", ".jp2", ".png", ".tif"]


#################################################
# Step 2 - Convert Images
#################################################
# check to see if the input images are in an acceptabe format, if so convert them, otherwise throw and error
if inFormat_ext in goodFormats:
    print("In files format match a supported format...Proceeding with conversion!")

    # make list of all images of the inFormat type specified above
    img_list = glob(inFolder + "/*{}".format(inFormat_ext))

    # convert each image in the folder to the outFormat listed above, and save the new image to the outFolder
    for img in img_list:
        # create the output file name & path
        tifName = img[:-4] + outFormat_ext
        outTif = tifName.replace(inFolder, outFolder)

        # convert the input raster using copy raster
        arcpy.CopyRaster_management(img, outTif)
        print("Successfully converted: {} to {}!".format(os.path.basename(img), outFormat_ext))

# raise an error if the input format does not match one of the acceptable image formats
else:
    raise Exception(
    "ERROR: Image format is not supported...Aborting Conversion Process."
    "\nOnly the following formats are supported inputs for this tool:"
    "\n.bil, .bip, .bmp, .bsq, .dat, .gif, .img, .jpg, .jp2, .png, .tif")
