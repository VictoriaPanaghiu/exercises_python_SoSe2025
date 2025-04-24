#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 11:19:40 2025

@author: vicsss19
"""

#übung zu slycing

quad_zahl=[]

for zahl in range(11): #oder 1,11
    print(zahl)
    if zahl % 2 == 1: #wenn ungerade
        quad_zahl.append(zahl**2)
    else:
        quad_zahl.append(zahl)  #wenn gerade
    
    
print(quad_zahl)


    
    
    
#testen ob zahl gerade oder ungerade mit modulo