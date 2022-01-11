# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 13:37:12 2021

@author: Admin
"""

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()