#!/usr/bin/env python
#encoding:utf-8

import numpy as np
import matplotlib.pyplot as plt

x=np.loadtxt('ALS_LNA_RAD_TSI_2002_2009_eps5_complet.asc', skiprows=1)

aa, mm, jj = x[:,0], x[:,1], x[:,2]
hh, mm = x[:,3], x[:,4]

cblow = x[:,9]
cbmid = x[:,10]
cbhigh = x[:,11]

plt.plot(cblow)

# probleme avec -999 ?
plt.clf()
cblow = np.ma.masked_where(cblow < 0, cblow)
plt.plot(cblow)

plt.show()