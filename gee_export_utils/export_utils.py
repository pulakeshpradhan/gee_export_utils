import ee
import os
import geemap

def export_image_to_drive(image, region, scale, crs='EPSG:4326', description='export'):
    """
    Export an Earth Engine image to Google Drive.
    """
    if region is None:
        region = roi.geometry()

    task = ee.batch.Export.image.toDrive(
        image=image.clip(region),
        description=description,
        folder='GEE_Exports',
        fileNamePrefix=description,
        region=region.bounds(),
        scale=scale,
        crs=crs,
        maxPixels=1e13
    )
    task.start()
    print(f"📤 Export started: {description}")

def download_image_single(image, region, scale, crs='EPSG:4326', output_dir='./'):
    """
    Download a single Earth Engine image as GeoTIFF.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    geemap.download_ee_image(
        image=image.clip(region),
        region=region,
        scale=scale,
        crs=crs,
        filename=os.path.join(output_dir, "output.tif")
    )
    print(f"📥 Image Downloaded Successfully.")

def download_image_tiles(image, region, scale, crs='EPSG:4326', output_dir='./', prefix="Image_", rows=2, cols=2, delta=0):
    """
    Download image tiles from an Earth Engine image using a mesh grid.
    """
    grids = geemap.fishnet(region, rows=rows, cols=cols, delta=delta)

    tiles_dir = os.path.join(os.path.abspath(output_dir), "tiles")

    geemap.download_ee_image_tiles(
        image=image,
        features=grids,
        out_dir=tiles_dir,
        prefix=prefix,
        crs=crs,
        scale=scale
    )
    print(f"📥 Image tiles saved to: {tiles_dir}")
