from matplotlib import pyplot as plt
from cartopy.io import img_tiles as cimgt
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


def add_map_subplot(
    fig: plt.Figure,
    nrows: int,
    ncols: int,
    index: int,
    tiles=cimgt.Stamen(),
    extent=(-180, 180, -90, 90),
    scale=5,
) -> plt.Axes:
    ax = fig.add_subplot(nrows, ncols, index, projection=tiles.crs)

    gl = ax.gridlines(
        draw_labels=True,
        xformatter=LONGITUDE_FORMATTER,
        yformatter=LATITUDE_FORMATTER,
        linestyle='dotted',
    )
    gl.top_labels = False
    gl.right_labels = False
    
    ax.set_extent(extent)
    ax.add_image(tiles, scale)
    
    return ax
