#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 18:50:50 2020

@author: amelielaurens
"""

from models_RJS import *

# Predict the critical rotational velocity for jet ejection
surface_tension = float(input("Enter the surface tension in kg/s^2 : "))
orifice_radius = float(input("Enter the radius of the orifice in m : "))
s0 = float(input("Enter the radius of the reservoir in m : "))
rho = float(input("Enter the density of the polymer in kg/m^3 : "))
critical_rotational_velocity = critical_rotational_velocity_threshold(surface_tension, orifice_radius, s0, rho)
print('The critical rotational velocity threshold for jet ejection is : %s (in round per second).' %(critical_rotational_velocity))
