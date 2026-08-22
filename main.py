import matplotlib.pyplot as plt
import drone_models
import utilities.physics as phys
import utilities.constants as consts

# Initial Conditions - maybe will move these to drone.py or constants.py later

simulation_time = 100 # s
initial_velocity = 0 # m/s
time = 0 # s
initial_position = 0 # m

# Storage Information

time_history = []
position_history = []
velocity_history = []

holybro_drone = drone_models.HolybroX650(
    initial_position=initial_position,
    initial_velocity=initial_velocity
)

holybro_drone.set_motor_thrusts([5.0, 5.0, 5.0, 5.0])

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