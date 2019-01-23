#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:23:37 2019

@author: cristina
"""
import numpy as np

N_atoms = 2
borde_x = 1
borde_y = 1

N_x = N_atoms + 2*borde_x
N_y = N_atoms + 2*borde_y

Self = np.zeros([N_y * N_x, N_y * N_x], dtype=float)

for j_atom in range(N_atoms):
    for i_atom in range(N_atoms):
         
         g_i = (j_atom + borde_y) * N_x + (i_atom + borde_x)
         Self [g_i, g_i]= 5.0
         
