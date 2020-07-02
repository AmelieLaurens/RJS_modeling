#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:27:46 2020

@author: amelielaurens
"""
from models_RJS import *

# Predict the critical rotational velocity for jet ejection
surface_tension = float(input("Enter the surface tension in g/s^2 : "))
orifice_radius = float(input("Enter the radius of the orifice in cm : "))
s0 = float(input("Enter the radius of the reservoir in cm : "))
rho = float(input("Enter the density of the polymer in g/cm^3 : "))
critical_rotational_velocity = critical_rotational_velocity(surface_tension, orifice_radius, s0, rho)
print('The critical rotational velocity for jet ejection is : %s (in round per min).' %(critical_rotational_velocity))