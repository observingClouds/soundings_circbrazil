import fsspec
import matplotlib.patches as mpatches
import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import xarray as xr

datapath = "zip://data/level2/CircBrazil_Sonne_soundings_level2_v1.0.0.nc::/work/mh0010/m300408/circBrazil_Soundings/data.zip"

cross_sections = {
    "ITCZ cross-section 1":
    {
        "soundings" : slice(2,68),
        "color": "blue"
    },
    "ITCZ cross-section 2":
    {
         "soundings" : slice(148, 226),
         "color": "red"
    },
    "ITCZ cross-section 3":
    {
        "soundings" : slice(225,256),
        "color": "orange"
    }
}

ds = xr.open_dataset(datapath)
ds = ds.sortby("launch_time")

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

ax.set_global()
ax.stock_img()
ax.coastlines()

ax.plot(-0.08, 51.53, 'o', transform=ccrs.PlateCarree())
mask_ascent = ds.ascent_flag.astype(bool)

colors = ['grey']*len(mask_ascent)
for cross_section, attr in cross_sections.items():
    colors[attr["soundings"]] = [attr["color"]]*(attr["soundings"].stop-attr["soundings"].start)

ax.scatter(ds.lon.values[~mask_ascent,0], ds.lat.values[~mask_ascent,0],
           c=np.array(colors)[~mask_ascent],transform=ccrs.PlateCarree(), marker='.')

patches = []*(len(cross_sections.keys())+1)
for section, attr in cross_sections.items():
    patches.append(mpatches.Patch(color=attr["color"], label=section))
patches.append(mpatches.Patch(color="grey", label="additional sondes"))
ax.legend(handles=patches)

plt.ylim(-20,30)
plt.xlim(-60,10)

gl = ax.gridlines(draw_labels=True)
gl.top_labels = False
gl.right_labels = False

plt.tight_layout()
plt.savefig("sounding_launch_positions.png", bbox_inches="tight")

