import matplotlib.pyplot as plt
import drone_models
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
acceleration_history = []
thrust_history = []

holybro_drone = drone_models.HolybroX650(
    initial_position=initial_position,
    initial_velocity=initial_velocity
)

holybro_drone.set_motor_throttles([0.7, 0.7, 0.7, 0.7])  # Set all motors to X% throttle

# Simulation loop

while time <= simulation_time:

    # Stores current state of drone before updating
    position, velocity = holybro_drone.get_status()

    # Storing data
    time_history.append(time)
    position_history.append(position)
    velocity_history.append(velocity)
    acceleration_history.append(holybro_drone.acceleration)
    thrust_history.append(holybro_drone.total_thrust)

    # Advance the simulation by one timestep
    holybro_drone.update_status()

    # Update time
    time += consts.TIMESTEP

print(
    f"Time: {time:.2f} s | "
    f"Thrust: {holybro_drone.total_thrust:.2f} N | "
    f"Weight: {-holybro_drone.gravitational_force:.2f} N | "
    f"Net force: {holybro_drone.net_force:.2f} N | "
    f"Acceleration: {holybro_drone.acceleration:.2f} m/s^2"
)

# Plot

plt.plot(time_history, position_history)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.grid()
plt.show()