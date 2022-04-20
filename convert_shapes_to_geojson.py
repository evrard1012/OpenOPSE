import sys
import geopandas as gpd

def convert_shapes_to_geojson(shapefilename,geojsonfilename):
    gdf = gpd.read_file(shapefilename)
    gdf.to_file(geojsonfilename)
geojsonfilename = sys.argv[1]
shapefilename = sys.argv[2]
convert_shapes_to_geojson(shapefilename,geojsonfilename)