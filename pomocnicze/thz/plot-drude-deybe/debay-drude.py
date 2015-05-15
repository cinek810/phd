#!/usr/bin/python

from pylab import *

def drude(f):
	eps_0=1
	sigma0=100
	tau=10e-12
	eps=eps_0+1j*sigma0/(f*(1-1j*f*tau))
	return eps


def debye(f):
	epsi=0
	eps0=1
	td=10e7
	eps=epsi+(eps0-epsi)/(1-1j*f*td)
	return eps

f=logspace(11, 14,num=100)
plot(f,real(drude(f)),'r-',f,real(debye(f)),'b-')
xscale('log')
show()
