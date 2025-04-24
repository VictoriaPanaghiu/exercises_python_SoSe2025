#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 09:07:27 2025

@author: vicsss19
"""

 #aufgabe nr 2 am 24. von folien aus letzter woche
 
def teilbar(x, y):
    if y== 0:
        print("Es ist nicht möglich durch 0 zu teilen")
    elif y == x:
        print("x und y sind gleich")
    else:
        if x%y == 0:
            print(x, "ist teilbar", y)
        else:
            print(x, "ist nicht teilbar durch", y)
            
teilbar(10, 0)



  
            
 
    
    
            
            

        
        
    