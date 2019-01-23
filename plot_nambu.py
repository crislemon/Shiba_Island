#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 17:02:00 2018

@author: cristina
"""

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 13})

def Nambu(spectro_up, spectro_down, spectro_uphole, spectro_downhole, vv, row, borde_x, borde_y):
    
    plt.figure(6)
    spectro_up_1 = spectro_up[borde_y, borde_x, :]
    spectro_down_1 = spectro_down[borde_y, borde_x, :]
    spectro_uphole_1 = spectro_uphole[borde_y, borde_x, :]
    spectro_downhole_1 = spectro_downhole[borde_y, borde_x, :]

    plt.plot(vv, spectro_up_1,label='Nambu 1',linewidth=0.8)
    plt.plot(vv, spectro_down_1,label='Nambu 2',linewidth=0.8)
    plt.plot(vv, spectro_uphole_1,label='Nambu 3',linewidth=0.8)
    plt.plot(vv, spectro_downhole_1,label='Nambu 4',linewidth=0.8)
    plt.legend()
    plt.xlabel('mV')
    plt.ylabel('PDOS')
    plt.title('Nambu components')
    plt.savefig('results/Nambu.pdf')