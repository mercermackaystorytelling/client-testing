# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 03:44:54 2020

@author: Gupta


This is a file for utility functions only. 
Utility functions increase readability of code by 
increasing reusability 


"""

import marketReport as mr
import basicClient as bc


import numpy
import scipy 
import matplotlib.pyplot as plt

from time import time
import pdb
import os

import pandas as pd








def converttopercent(fraction):
        if fraction<0:
            return "cannot convert, negative fraction"
        else:
            return fraction * 100





































