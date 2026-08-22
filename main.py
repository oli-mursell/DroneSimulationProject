import matplotlib.pyplot as plt
import drone_models
import utilities.physics as phys
import utilities.constants as consts

# Initial Conditions - maybe will move these to drone.py or constants.py later

simulation_time = 10 # s
initial_velocity = 10 # m/s
time = 1 # s
initial_position = 500 # m

# Storage Information

time_history = []
position_history = []
velocity_history = []

holybro_drone = drone_models.HolybroX650(
    initial_position=initial_position,
    initial_velocity=initial_velocity
)

# Simulation loop

while time <= simulation_time:

    # Calculate the forces
    Fg = holybro_drone.gravitational_force
    Fnet = phys.net_forces([Fg])

    # Calculate acceleration
    acceleration = holybro_drone.acceleration

    # Calculate position and velocity
    holybro_drone.update_status()

    # Update time
    time += consts.TIMESTEP

    # Storing data
    time_history.append(time)
    position_history.append(holybro_drone.get_status()[0])
    velocity_history.append(holybro_drone.get_status()[1])

# Plot

plt.plot(time_history, position_history)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.grid()
plt.show()