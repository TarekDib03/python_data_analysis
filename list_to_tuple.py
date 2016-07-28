# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 01:17:41 2016

@author: hduser
"""

def list_to_tuples(MY_LIST):
    
    for LIST in MY_LIST:
        # Reverse each of the inner lists
        LIST = LIST.reverse()
    
    for i in range(0, len(MY_LIST)):
        # Convert each of the inner list into tuple
        MY_LIST[i] = tuple(MY_LIST[i])
    return tuple(MY_LIST)