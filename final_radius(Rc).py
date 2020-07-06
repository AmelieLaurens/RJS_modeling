#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:06:17 2020

@author: amelielaurens
"""
from models_RJS import *
import numpy
import matplotlib.pyplot as plt

# Predict an approximation of the final radius for various collector distances
s0 = float(input("Enter the radius of the reservoir in m : "))
surface_tension =float(input("Enter the surface tension in kg/s^2 : "))
orifice_radius = float(input("Enter the radius of the orifice in m : "))
rho = float(input("Enter the density of the polymer in kg/m^3 : "))
omega_th=critical_rotational_velocity_threshold(surface_tension, orifice_radius, s0, rho)
initial_velocity=Initial_velocity(omega_th, s0)
mu = float(input("Enter the viscosity of the polymer in Pa.s : "))
nu = kinematic_viscosity(mu, rho)
omega = float(input("Enter the angular velocity in rounds per second : "))
discretisation = int(input("Enter an int for the mesh's thinness : "))
Rc = numpy.linspace(0.09, 0.18, discretisation)


final_radius = []
for k in range(discretisation):
    final_radius.append(final_radius_approx(orifice_radius, initial_velocity, nu, Rc[k], omega))
final_radius=numpy.array(final_radius)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

for i in range(discretisation):
    axes.plot(Rc[i], final_radius[i], 'ro')
axes.grid()
axes.set_xlabel("Collector distance (m)", fontsize=16)
axes.set_ylabel("Final radius (m)", fontsize=16)
axes.set_title("Final radius as a function of the collector distance ", fontsize=16)