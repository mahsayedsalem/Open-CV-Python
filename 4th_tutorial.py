# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 01:50:50 2018

@author: mahssalem
"""

import numpy as np
import cv2

img = cv2.imread('img.jpg', cv2.IMREAD_COLOR)

img[55,55]=[255,255,255]
px = img[55, 55]
print(px)

