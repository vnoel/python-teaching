
import netCDF4

# lecture des donnees
nc = netCDF4.Dataset('t2.2002.asm.nc')
lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
t2 = nc.variables['t2'][:]

whos
print t2.shape

t2 = t2.mean(axis=0)

# affichage
pcolor(lon, lat, t2)
xlim(0, 360)
ylim(-90, 90)
colorbar()