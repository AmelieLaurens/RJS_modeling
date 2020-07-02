#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:24:06 2020

@author: amelielaurens
"""
from math import *

def critical_rotational_velocity(surface_tension, orifice_radius, s0, rho):
    """RJS
        
    :Input:
    - *surface_tension* (float) - surface tension (g/s^2)
    - *orifice_radius* (float) - radius of the orifice (cm)
    - *s0* (float) - radius of the reservoir (cm)
    - *rho* (float) - density (g/cm^3)
         
    :Returns:
    (float) - Critical rotational speed for jet ejection (tours par seconde)
         
    """
    return 60*sqrt(surface_tension/(orifice_radius**2*s0*rho))
    

def sigma(surface_tension, x_position, r0, initial_velocity):
    """RJS
        
    sigma=surface_tension * x_position / (r0 * initial_velocity)
        
    :Input:
    - *surface_tension* (float) - surface tension (g/s^2)
    - *x_position* (float) - axial coordinate x (m)
    - *r0* (float) - initial radius of the jet = orifice radius a (m)
    - *initial_velocity* (float) - initial axial velocity (m/s)
         
    :Returns:
    (float) - sigma
         
    """
    return surface_tension * x_position / (r0 * initial_velocity)


def final_radius(r0, rho, initial_velocity, x_position, mu, Sigma, omega):
    """RJS
        
    :Input:
    - *r0* (float) - initial radius of the jet = orifice radius a (m)
    - *rho* (float) - density (kg/m^3)
    - *initial_velocity* (float) - initial axial velocity (m/s)
    - *x_position* (float) - axial coordinate x (m)
    - *mu* (float) - viscosity (Pa.s)
    - *Sigma* (float) - call sigma function : sigma(surface_tension, x_position, r0, initial_velocity)
    - *omega* (float) - angular velocity (Pa.s)
         
    :Returns:
    (float) - final radius (m)
         
    """
    return r0*sqrt(rho*initial_velocity*x_position/(mu-Sigma+sqrt((mu-Sigma)**2+(rho*omega*x_position**2)**2)))


def final_radius_approx(r0, initial_velocity, nu, Rc, omega):
    """RJS
        
    :Input:
    - *r0* (float) - initial radius of the jet = orifice radius a (m)
    - *initial_velocity* (float) - initial axial velocity (m/s)
    - *nu* (float) - kinematic viscosity (m^2/s) : call kinematic_viscosity function : 
    - *Rc* (float) - radius of the collector (m)
    - *omega* (float) - angular velocity (Pa.s)
         
    :Returns:
    (float) - approximation of the final radius  (m)
         
    """
    return r0*sqrt(initial_velocity*nu)/(Rc**(3/2)*omega)


def kinematic_viscosity(mu, rho):
    """RJS
        
    :Input:
    - *mu* (float) - viscosity (Pa.s) 
    - *rho* (float) - density (kg/m^3)
         
    :Returns:
    (float) - kinematic viscosity (m^2/s)
         
    """
    return mu/rho
    

    