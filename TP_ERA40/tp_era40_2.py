import netCDF4
from mpl_toolkits.basemap import Basemap

# lecture des donnees
nc = netCDF4.Dataset('t2.2002.asm.nc')
lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
t2 = nc.variables['t2'][:]

whos
print t2.shape
t2 = t2.mean(axis=0)

# carte globale

m = Basemap()
xlon, xlat = m(lon, lat)
m.pcolor(x, y, t2)
m.drawcoastlines()
cb = colorbar()
cb.set_label('Temperature a 2m')

# Astuce pour faire boucler les longitudes...
from mpl_toolkits.basemap import shiftgrid
t2, lon = shiftgrid(-180., t2, lon-360)


# carte zoomee France
figure()
m = Basemap(llcrnrlon=-7.,llcrnrlat=41,urcrnrlon=12,urcrnrlat=51.5,
           resolution='i',lon_0=2.5,lat_0=46.25,lat_ts=0)
xlon, xlat = m(lon, lat)
m.pcolor(x, y, t2)
m.drawcoastlines(color='white')
m.drawcountries(color='white')
m.drawmeridians(r_[-180:180:2.5], labels=[0,0,0,1], color='grey')
m.drawparallels(r_[-90:90:2.5], labels=[1,0,0,0], color='grey')
m.drawmapboundary(color='k', linewidth=2.0)
cb = colorbar()
cb.set_label('Temperature - ' + nc.variables['t2'].units)

savefig('figure2.png')