# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:36:29 2024

@author: nmurphy
"""
from scipy import signal
import numpy as np
import scipy as sp
from scipy import io
from thoi.measures.gaussian_copula import multi_order_measures

"""
Use this part to set the path --- change to your own storage location

In the final version we will interrogate the folder contents to select the data we want and loop through

"""
datapath = '/Users/krisha/Desktop/BCM/Analysis/HOI_implementation/project-eeg-hoi/Data/'
subj17_RS_baseline = 'VA-LLK-017-1_1_EEG_RS_DAY1.mat'
subj17_RS_postket = 'VA-LLK-017-1_2_EEG_RS_DAY1.mat'

"""
Load the data

In the final version we will loop through the folder contents variable to load each file
"""
S1_Data1 = sp.io.loadmat(datapath+subj17_RS_baseline)
S1_Data2 = sp.io.loadmat(datapath+subj17_RS_baseline)

"""
Process Time 1

We have the following
- Theta
- Alpha
- Beta
- Gamma
- whole band

The data needs to be organized to be timepoints x chans

Rather than create lots of variables we are simply calling the transposed
matrix from within the dictionary inside the function for multi order measures.
"""

T1_Theta =  multi_order_measures(S1_Data1['Theta'].transpose())
T1_Alpha = multi_order_measures(S1_Data1['Alpha'].transpose())
T1_Beta = multi_order_measures(S1_Data1['Beta'].transpose())
T1_Gamma = multi_order_measures(S1_Data1['Gamma'].transpose())
T1_WholeBand = multi_order_measures(S1_Data1['Wholeband'].transpose())

"""
Process Time 2

"""

T2_Theta =  multi_order_measures(S1_Data2['Theta'].transpose())
T2_Alpha = multi_order_measures(S1_Data2['Alpha'].transpose())
T2_Beta = multi_order_measures(S1_Data2['Beta'].transpose())
T2_Gamma = multi_order_measures(S1_Data2['Gamma'].transpose())
T2_WholeBand = multi_order_measures(S1_Data2['Wholeband'].transpose())

print(T2_Theta)

"""
Create Effect Sizes

I want to review what the data looks like before we estimate how to do this

"""
