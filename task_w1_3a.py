# -*- coding: utf-8 -*-
"""Task-W1-3A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VPN0ugYaMMrFsi8SPYUFhq2kAmAlIUA0

Task W1 3A: Task-W1-3A:Please write a piece of code that will generate numbers for a coupon in Sayisal Loto that should inlude 8 colons
and each column should have 6 random numbers.Please control the colons in terms of having no repetitions.
"""

import numpy as np

x =  np.random.randint(1,50, size=(6,8))

i=0
j=0
l=0
for i in range(6):
  for j in range(8):
    for l in range(1,8,1):
        if x[i][j] == x[i][l]:
          continue
        elif x[i][j] == x[i][l]:
          x[i][j] = np.random.randint(1,50,1)
        else:
          continue

x
