#!/usr/bin/python

from numpy import linspace,exp,real,imag,hstack
import pylab as plt

import matplotlib
matplotlib.rcParams.update({'font.size': 30})


k=3
x=linspace(0,10,200)
y=exp(1j*x*k)

plt.figure()
plt.plot(real(x),imag(x),lw=3)
plt.xlabel("Re(x)")
plt.ylabel("Im(x)")
plt.tight_layout()
plt.savefig("../../../images/pml/real-x.png")

plt.figure()
plt.plot(x,y,lw=3)
plt.xlabel("Re(x)")
plt.ylabel("exp(ikx)")
plt.tight_layout()
plt.savefig("../../../images/pml/real-x-wave.png")

x=linspace(0,5)
x2=linspace(5,10)+1j*(linspace(0,1))
x=hstack((x, x2))
y=exp(1j*x*k)

plt.figure()
plt.plot(real(x),imag(x),lw=3)
plt.xlabel("Re(x)")
plt.ylabel("Im(x)")
plt.tight_layout()
plt.savefig("../../../images/pml/complex-x.png")

plt.figure()
plt.plot(x,y,lw=3)
plt.xlabel("Re(x)")
plt.ylabel("exp(ikx)")
plt.tight_layout()
plt.savefig("../../../images/pml/complex-x-wave.png")




#plt.show()
