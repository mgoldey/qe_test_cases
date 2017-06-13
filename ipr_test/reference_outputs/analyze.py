import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import sys

from numpy import pi

for fn in sys.argv[1:]:
    print fn
    a=open(fn,'r').read()
    a=a[a.index("\n")+1:]
    a=a[a.index("\n")+1:]
    nat=int(a[0:a.index("\n")].split()[0])
    a=a[a.index("\n")+1:]
    nr1=int(a[0:a.index("\n")].split()[0])
    a1=np.array(a[0:a.index("\n")].split()[1:],dtype='float')
    l1=nr1*a1[0]
    a=a[a.index("\n")+1:]
    nr2=int(a[0:a.index("\n")].split()[0])
    a2=np.array(a[0:a.index("\n")].split()[1:],dtype='float')
    l2=nr2*a2[1]
    a=a[a.index("\n")+1:]
    nr3=int(a[0:a.index("\n")].split()[0])
    a3=np.array(a[0:a.index("\n")].split()[1:],dtype='float')
    l3=nr3*a3[2]
    a=a[a.index("\n")+1:]
    dim=[l1,l2,l3]

    def box(x,y,z):
        x[np.where((x)>dim[0]/2.)]-=dim[0]
        y[np.where((y)>dim[1]/2.)]-=dim[1]
        z[np.where((z)>dim[2]/2.)]-=dim[2]

        x[np.where((x)<-dim[0]/2.)]+=dim[0]
        y[np.where((y)<-dim[1]/2.)]+=dim[1]
        z[np.where((z)<-dim[2]/2.)]+=dim[2]
        return

    #move to data
    for i in range(nat):
        a=a[a.index("\n")+1:]

    #process
    b=np.array(a.strip().split(),dtype=float)

    denom=np.dot(b,b)
    b/=np.sqrt(denom)

    #cube files are z,y,x
    c=b.reshape(nr1,nr2,nr3)

    x,y,z = np.ogrid[0:l1:a1[0],0:l2:a2[1],0:l3:a3[2]]
    x=x.flatten()[:nr1]
    y=y.flatten()[:nr2]
    z=z.flatten()[:nr3]
    c2=c

    fac=2.0*np.pi/(l1)
    valx=np.dot(np.sum(np.sum(c2,axis=1),axis=1),(np.exp(x*fac*np.complex(1j))))
    valx=np.imag(np.log(valx))/fac

    fac=2.0*np.pi/(l2)
    valy=np.dot(np.sum(np.sum(c2,axis=2),axis=0),(np.exp(y*fac*np.complex(1j))))
    valy=np.imag(np.log(valy))/fac

    fac=2.0*np.pi/(l3)
    valz=np.dot(np.sum(np.sum(c2,axis=0),axis=0),(np.exp(z*fac*np.complex(1j))))
    valz=np.imag(np.log(valz))/fac

    if (valx<0.0):
        valx+=l1
    if (valy<0.0):
        valy+=l2
    if (valz<0.0):
        valz+=l3
    print(valx*0.529177,valy*0.529177,valz*0.529177)
