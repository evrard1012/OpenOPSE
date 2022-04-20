import skimage.io as io
import skimage
import scipy.misc
import glymur
import numpy
from PIL import Image
from pathlib import Path
import sys
import os

def resizebmp(bmpi, L, size=500):
    img = Image.fromarray((bmpi * 255).astype(numpy.uint8), mode=None)
    bmpo = img.resize((size,size))
    bmpo = numpy.array(bmpo)
    return bmpo
def savetopng(src,dst, size=500,as_gray=True):    
    #outputname = "{}.png".format(filename.split('.tif')[0])
    bmp = io.imread(src,as_gray=as_gray, plugin='tifffile')
    bmpt = resizebmp(bmp, 200, size)
    data = Image.fromarray(bmpt)
    data.save(dst)

src = sys.argv[1]
dest = src+'thumbnails/'
Path(dest).mkdir(parents=True, exist_ok=True)
Image.MAX_IMAGE_PIXELS = None
list_of_files = filter( lambda x: os.path.isfile(os.path.join(src, x)),os.listdir(src) )
# Create a list of files in directory along with the size
files_with_size = [ (file_name, os.stat(os.path.join(src, file_name)).st_size) for file_name in list_of_files  ]
for file_name, size in files_with_size:
    dst = (dest+file_name).split('.')[0] + '.png'
    source = src+file_name
    savetopng(source, dst)
