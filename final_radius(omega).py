#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:27:46 2020

@author: amelielaurens
"""
from models_RJS import *
import numpy
import matplotlib.pyplot as plt



# Predict an approximation of the final radius for various angular velocities
orifice_radius = float(input("Enter the radius of the orifice in m : "))
initial_velocity = float(input("Enter the initial axial velocity in m/s : "))
mu = float(input("Enter the viscosity of the polymer in Pa.s : "))
rho = float(input("Enter the density of the polymer in kg/m^3 : "))
nu = kinematic_viscosity(mu, rho)
Rc = float(input("Enter the radius of the collector in m : "))
discretisation = int(input("Enter an int for the mesh's thinness : "))
omega = numpy.linspace(4000//60, 37000//60, discretisation)
final_radius = []
for k in range(discretisation):
    final_radius.append(final_radius_approx(orifice_radius, initial_velocity, nu, Rc, omega[k]))
final_radius=numpy.array(final_radius)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

for i in range(discretisation):
    axes.plot(omega[i], final_radius[i], 'ro')
axes.grid()
axes.set_xlabel("Angular velocity (rounds per second)", fontsize=16)
axes.set_ylabel("Final radius (m)", fontsize=16)
axes.set_title("Final radius as a function of the angular velocity ", fontsize=16)

