#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 17:24:47 2018

@author: cristina
"""

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
plt.rcParams.update({'font.size': 13})

def map2D_3D(z, z_up, z_down, z_x, z_13, z_24, titulo, N_x, N_y, N_omega, vv):
    
    #2D plots
    plt.figure(7)
    plt.imshow(z, cmap = plt.cm.jet)
    plt.colorbar(orientation='horizontal')
    plt.title('FM E = %f meV' %titulo)
    plt.savefig('results/2D.pdf')
    
#    plt.figure(6)
#    plt.imshow(z_up, cmap = plt.cm.jet)
#    plt.colorbar(orientation='horizontal')
#    plt.title('Spin up' %titulo)
#    plt.savefig('results/2D_up.pdf')
#    
#    plt.figure(7)
#    plt.imshow(z_down, cmap = plt.cm.jet)
#    plt.colorbar(orientation='horizontal')
#    plt.title('Spin down' %titulo)
#    plt.savefig('results/2D_down.pdf')
#    
    plt.figure(8)
    plt.imshow(z_x, cmap = plt.cm.jet)
    plt.colorbar(orientation='horizontal')
    plt.title('Spin x')
    plt.savefig('results/2D_x.pdf')
    
    plt.figure(9)
    plt.imshow(z_up - z_down, cmap = plt.cm.jet)
    plt.colorbar(orientation='horizontal')
    plt.title('Spin z')
    plt.savefig('results/2D_z.pdf')
    
    plt.figure(10)
    plt.imshow(z_13 - z_24, cmap = plt.cm.jet)
    plt.colorbar(orientation='horizontal')
    plt.title('Spin 13 - 24')
    plt.savefig('results/2D_13.pdf')
    
    
    #################
    #################
    
    
    
    #3D plot
    Y = list(range(N_y))
    X = list(range (N_x))
    X, Y = np.meshgrid(X, Y)
    fig2 = plt.figure(11)
    ax = fig2.add_subplot((111), projection='3d')
    ax.plot_wireframe(X, Y, z)
    plt.title('FM E = %f meV' %titulo)
    ax.set_zlabel('PDOS')
    plt.savefig('results/3D.pdf')
