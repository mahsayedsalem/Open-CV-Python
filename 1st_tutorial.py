# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 01:04:23 2018

@author: mahssalem
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
#IMREAD_GRAYSCALE = 0, IMREAD_COLOR=1, IMREAD_UNCHANGED=-1

#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.plot([50,100],[80,100], 'c', linewidth=5)
#plt.show()

cv2.imwrite('imggray.png', img)