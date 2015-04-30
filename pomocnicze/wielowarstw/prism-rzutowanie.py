#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pylab as plt

x=np.linspace(-30,30,100)
#FWHM funkcji odpowiedzi implusowej
FWHM=10
s=FWHM/2.335
y=np.exp(-x*x/4/(s*s))/s/np.sqrt(2*np.pi)

otw=np.zeros(x.size)
rozmiar=10
odstep=30
otw[otw.size/2-odstep/2-rozmiar/2:otw.size/2-odstep/2+rozmiar/2]=1
otw[otw.size/2+odstep/2-rozmiar/2:otw.size/2+odstep/2+rozmiar/2]=1

yy=np.convolve(y,otw,mode="same")

f,axarr=plt.subplots(2,sharex=True)
axarr[0].plot(x,otw)
axarr[0].axis([-30, 30,0,1.1])
print x.size
print y.size
axarr[1].plot(x,yy)
plt.xlabel(u'położenie [nm]')
#FWHMline=np.ones(yy.size)*max(yy)/2
#plt.plot(x,FWHMline)
plt.show()

