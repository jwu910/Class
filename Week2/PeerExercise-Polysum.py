#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 13:39:17 2017

@author: joshua
"""

import math
m = math
def polysum(n,s):
    """
    function should take two arguments 'n' number of sides and 's' length of polygon side
    function will return area of polygon + perimeter squared rounded to 4 dec places.
    """
    return round(((0.25 * n * (s**2))/(m.tan(m.pi/n))) + (s * n)**2,4)