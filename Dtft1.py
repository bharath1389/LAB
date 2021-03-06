#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 13:54:00 2019

@author: apiiit-rkv
"""

import numpy as np
from matplotlib import pyplot as plt
import cmath as c
j=c.sqrt(-1)
t=np.linspace(0,2,50)
x=np.sin(2*np.pi*t)
d=len(x)
b=[]
p=[]
q=[]
w=np.linspace(-np.pi,np.pi,1000)
for k in range (0,1000,1):
    s=0
    for i in range(0,d,1):
        s=s+((x[i]*(np.exp(-j*w[k]*i))))
    b.append(s)
    p.append (abs(s))
    q.append (np.angle(s))
plt.subplot (411)
plt.stem(t,x)
plt.subplot (412)
plt.plot (w,b)
plt.subplot (413)
plt.plot (w,p)
plt.subplot (414)
plt.plot (w,q)