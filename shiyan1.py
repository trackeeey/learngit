#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####一元二次方程的解
import math
def a(a,b,c):
	m=math.sqrt(b**2-4*a*c)
	x1=(-b+m)/(2*a)
	x2=(-b-m)/(2*a)
	return x1,x2

print (a(1,3,-4))
