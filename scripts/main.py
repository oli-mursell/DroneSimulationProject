import matplotlib.pyplot as plt
from physics import (gravity_force, net_forces, calculate_acceleration, update_position, update_velocity)
from constants import GRAVITY, TIMESTEP

# Initial Conditions - maybe will move these to drone.py or constants.py later

mass = 1 # kg 
velocity = 10 # m/s
position = 500 # m
time = 0 # s
simulation_time = 10 # s

# Storage Information

time_history = []
position_history = []
velocity_history = []

# Simulation loop

while time < simulation_time:

    # Calculate the forces
    Fg = gravity_force(mass)

    Fnet = net_forces([Fg])

    # Calculate acceleration
    acceleration = calculate_acceleration(Fnet, mass)

    # Calculate position and velocity
    velocity = update_velocity(velocity, acceleration, TIMESTEP)

    position = update_position(position, velocity, TIMESTEP)

    # Storing data
    time_history.append(time)
    position_history.append(position)
    velocity_history.append(velocity)

    # Update time
    time += TIMESTEP

# Plot

plt.plot(time_history, position_history)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.grid()
plt.show()