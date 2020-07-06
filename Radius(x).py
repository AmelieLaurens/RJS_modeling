#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:10:31 2020

@author: amelielaurens
"""

from models_RJS import *
import numpy
import matplotlib.pyplot as plt

# predict the radius of the jet in steady state as a function of the axial coordinate x
surface_tension =float(input("Enter the surface tension in g/s^2 : "))
Rc = float(input("Enter the radius of the collector in m : "))
discretisation = int(input("Enter an int for the mesh's thinness : "))
x_position = numpy.linspace(0, Rc, discretisation)
r0 = float(input("Enter the radius of the orifice in m : "))
initial_velocity = float(input("Enter the initial axial velocity in m/s : "))
Sigma = []
for l in range(discretisation):
    Sigma.append(sigma(surface_tension, x_position[l], r0, initial_velocity))
Sigma=numpy.array(Sigma)    
rho = float(input("Enter the density of the polymer in kg/m^3 : "))
mu = float(input("Enter the viscosity of the polymer in Pa.s : "))
omega = float(input("Enter the angular velocity in rounds per second : "))


radius=[]
for k in range(discretisation):
    radius.append(radius(r0, rho, initial_velocity, x_position[k], mu, Sigma[k], omega)
radius = numpy.array(radius)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

for i in range(discretisation):
    axes.plot(x_position[i], radius[i], 'ro')
axes.grid()
axes.set_xlabel("Axial coordinate x (m)", fontsize=16)
axes.set_ylabel("Radius (m)", fontsize=16)
axes.set_title("Radius of the jet as a function of the axial coordinate ", fontsize=16)