import matplotlib.pyplot as plt
import utilities.physics as phys
import utilities.constants as consts
from drone import Drone

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

skydiox10d = Drone()

# Simulation loop

while time < simulation_time:

    # Calculate the forces
    Fg = phys.gravity_force(skydiox10d.mass)

    Fnet = phys.net_forces([Fg])

    # Calculate acceleration
    acceleration = phys.calculate_acceleration(Fnet, skydiox10d.mass)

    # Calculate position and velocity
    velocity = phys.update_velocity(skydiox10d.velocity, acceleration, consts.TIMESTEP)

    position = phys.update_position(skydiox10d.position, velocity, consts.TIMESTEP)

    # Storing data
    time_history.append(time)
    position_history.append(position)
    velocity_history.append(velocity)

    # Update time
    time += consts.TIMESTEP

# Plot

plt.plot(time_history, position_history)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.grid()
plt.show()