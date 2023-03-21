# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 15:23:24 2023

@author: nkk
"""

from rio_tiler.io import Reader
import rasterio as rio

minX, minY = 353386.3, 4830677.4
maxX, maxY = 359907.0, 4836581.8

rst = r"C:\Users\nkk\data\bugs\riotiler\data\bouconne.tif"
rio_transform = rio.open(rst).transform
print(rio_transform)
# =============================================================================
# >>> | 30.00, 0.00, 350205.00|
# >>> | 0.00,-30.00, 4837995.00|
# >>> | 0.00, 0.00, 1.00|
#
# =============================================================================
image = Reader(rst)
arr = image.point(minX, minY, coord_crs=image.crs)
arr = image.part(
    [minX, minY, maxX, maxY], dst_crs=image.crs, bounds_crs=image.crs
)

rio_tiler_transform = arr.transform
print(rio_tiler_transform)
# =============================================================================
# >>> | 30.05, 0.00, 353386.30|
# >>> | 0.00,-29.97, 4836581.80|
# >>> | 0.00, 0.00, 1.00|
# =============================================================================
