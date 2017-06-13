# PLOT RADIAL DOS
import os
import numpy as np
from pylab import *
fl=os.popen("ls pospro_*").read().split()
Rmax=float(os.popen("grep \"radial d\" rad_avg.out").read().split()[-2])

def get_dos(ifl):
    data=np.array(open(ifl).read().split(),dtype=float)
    ld=len(data)//2
    data=data.reshape(ld,2)
    ens=data[:,0]
    dos=data[:,1]
    return [ens,dos]

full_dos=[]
for ifl in fl:
    ens,dos=get_dos(ifl)
    full_dos.append(dos)

full_dos=np.array(full_dos).T
Rs=np.arange(120)*Rmax/120.

X,Y=np.meshgrid(Rs,ens)
plt.contour(X,Y,full_dos)
plt.show()
