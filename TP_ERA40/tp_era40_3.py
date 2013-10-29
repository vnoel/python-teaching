import netCDF4
from mpl_toolkits.basemap import Basemap

# lecture de toutes les donnees - 1970-2002
files = glob.glob('t2.*.asm.nc')
files.sort()
t2_liste = []
for f in files[:-1]:
    # avoid 2002 (not same size)
    nc = netCDF4.Dataset(f)
    lat = nc.variables['lat'][:]
    lon = nc.variables['lon'][:]
    t2 = nc.variables['t2'][:]
    t2_year = t2.mean(axis=0)
    t2_liste.append(t2_year)

t2 = array(t2_liste)
t2_average = t2.mean(axis=0)

# anomalie pour 1976
anom76 = t2[6,...] - t2_average

# carte zoomee France
figure()
m = Basemap(llcrnrlon=-7.,llcrnrlat=41,urcrnrlon=12,urcrnrlat=51.5,
           resolution='i',lon_0=2.5,lat_0=46.25,lat_ts=0)
x, y = m(lon, lat)
m.pcolor(x, y, anom76)    
m.drawcoastlines(color='white')
m.drawcountries(color='white')
m.drawmeridians(r_[-180:180:2.5], labels=[0,0,0,1], color='grey')
m.drawparallels(r_[-90:90:2.5], labels=[1,0,0,0], color='grey')
m.drawmapboundary(color='k', linewidth=2.0)

cb = colorbar()
cb.set_label('Temperature - ' + nc.variables['t2'].units)

savefig('figure3.png')
 