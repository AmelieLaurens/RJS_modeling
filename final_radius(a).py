#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:25:04 2020

@author: amelielaurens
"""


from models_RJS import *
import numpy
import matplotlib.pyplot as plt

# Predict an approximation of the final radius for various orifice radius
initial_velocity = float(input("Enter the initial axial velocity in m/s : "))
mu = float(input("Enter the viscosity of the polymer in Pa.s : "))
rho = float(input("Enter the density of the polymer in kg/m^3 : "))
nu = kinematic_viscosity(mu, rho)
Rc = float(input("Enter the radius of the collector in m : "))
omega = float(input("Enter the angular velocity in rounds per second : "))
discretisation = int(input("Enter an int for the mesh's thinness : "))
orifice_radius = numpy.linspace(0.0001, 0.001, discretisation)


final_radius = []
for k in range(discretisation):
    final_radius.append(final_radius_approx(orifice_radius[k], initial_velocity, nu, Rc, omega))
final_radius=numpy.array(final_radius)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

for i in range(discretisation):
    axes.plot(orifice_radius[i], final_radius[i], 'ro')
axes.grid()
axes.set_xlabel("Radius of the orifice (m)", fontsize=16)
axes.set_ylabel("Final radius (m)", fontsize=16)
axes.set_title("Final radius as a function of the orifice radius ", fontsize=16)