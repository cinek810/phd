#!/usr/bin/python
import sys
from numpy import linspace
eps1=float(sys.argv[1])
eps2=float(sys.argv[2])

for f in linspace(0.1,0.9,20):

	epspa=f*eps1+(1-f)*eps2
	epspe=(f/eps1+(1-f)/eps2)**-1

	print "f="+str(f)+" epspa="+str(epspa)+" epspe="+str(epspe)
