import sys
import geopandas as gpd

def convert_geojson_to_shapes(shapefilename,geojsonfilename):
    gdf = gpd.read_file(geojsonfilename)
    gdf.to_file(shapefilename)

geojsonfilename = sys.argv[1]
shapefilename = sys.argv[2]
convert_geojson_to_shapes(shapefilename,geojsonfilename)