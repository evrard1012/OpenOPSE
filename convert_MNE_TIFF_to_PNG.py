import skimage.io as io
import skimage
import scipy.misc
import glymur
import numpy
from PIL import Image
from pathlib import Path
import sys
import os

def tnails(src, dest, filename,size=(500,500)):
    try:
        image = Image.open(src+filename).convert("RGB")
        image.thumbnail(size)
        dst = (dest+filename).split('.')[0] + '.png'
        image.save(dst)
    except IOError:
        pass

src = sys.argv[1]
dest = src+'thumbnails/'
Path(dest).mkdir(parents=True, exist_ok=True)
Image.MAX_IMAGE_PIXELS = None
# Get list of all files only in the given directory
list_of_files = filter( lambda x: os.path.isfile(os.path.join(src, x)),os.listdir(src) )
# Create a list of files in directory along with the size
files_with_size = [ (file_name, os.stat(os.path.join(src, file_name)).st_size) for file_name in list_of_files  ]
# Iterate over list of files along with size 
# and print them one by one.
for file_name, size in files_with_size:
    tnails(src, dest, file_name,size=(1000,1000))