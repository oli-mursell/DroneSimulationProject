import numpy as np
import constants

""" Contains the physics equations used in the simulation."""

# GRAVITY FORCE

def gravity_force(mass):
    """
    Calculates the force of gravity on an object given its mass.
    
    Parameters:
    mass : float (kg)

    Returns:
    force : float (N)
    """
    return -mass * constants.GRAVITY

# SUM OF FORCES

def net_forces(forces):
    """
    Sum of all forces acting on the object.
    
    Parameters:
    forces : list

    Returns:
    Net force : float (N)
    """
    return np.sum(forces)

# NEWTON'S 2ND LAW

def calculate_acceleration(force, mass):
    """
    Newton's 2nd Law: a = F/m 

    Parameters:
    force : float (N)
    mass : float (kg)

    Returns:
    Acceleration : float (m/s^2)
    """
    return force / mass

# UPDATED VELOCITY - EULER METHOD

def update_velocity(velocity, acceleration, dt):
    """
    Updates velocity of the object given its acceleration and dt.
    v = v0 + a*dt
    
    Parameters:
    velocity : float (m/s)
    acceleration : float (m/s^2)
    dt : float (s)

    Returns:
    Updated velocity : float (m/s)
    """
    return velocity + acceleration*dt

# UPDATED POSITION - EULER METHOD

def update_position(position, velocity, dt):
    """Updates position of the object given its velocity and dt.
    x = x0 + v*dt
    
    Parameters:
    position : float (m)
    velocity : float (m/s)
    dt : float (s)

    Returns:
    Updated position : float (m)
    """
    return position + velocity*dt