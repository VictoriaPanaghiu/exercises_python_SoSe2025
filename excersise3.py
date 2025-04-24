#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 09:44:45 2025

@author: vicsss19
"""

#listen
def steigung_funktion(meine_liste):
    x1 = meine_liste[0] #0 ist ein index
    y1 = meine_liste[1]
    x2 = meine_liste[2]
    y2 = meine_liste[3]
    delta_x = x2 - x1
    delta_y = y2 - y1
    
    if delta_x == 0:
        print("Die steigung ist nicht definiert")
    else:
        steigung = delta_y / delta_x
        return steigung
    
test_list = [4, 4, 8, 5]
    
    
print(steigung_funktion(test_list))



  
    
    
    
    
    
    
    