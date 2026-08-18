""" Contains the Drone class and its data """

class Drone:
    """
    Represents a quadcopter and its physical properties.

    This class stores:
        1. Physical properties of the drone
        2. Current state of drone during a simulation
    """
    def __init__(
            self, 
            mass=1.5,
            name="Quadcopter",
            arm_length=None,
            body_length=None,
            body_width=None,
            body_height=None,
            max_motor_speed=None,
            thrust_coefficient=None, 
        ):
        
        # Mass of the drone in kg
        self.mass = mass

        # Identifying name of the drone
        self.name = name

        # Physical dimensions of the drone
        self.arm_length = arm_length
        self.body_length = body_length
        self.body_width = body_width
        self.body_height = body_height

        # Maximum motor rotational speed in RPM
        self.max_motor_speed = max_motor_speed

        # Motor speeds - Front left = 1, Front right = 2, Rear left = 3, Rear right = 4
        self.motor_speeds = [0.0, 0.0, 0.0, 0.0]

        # Thrust coefficient for the drone
        self.thrust_coefficient = thrust_coefficient

        # Vertical Position in metres
        self.position = 0

        # Vertical Velocity in metres/second
        self.velocity = 0

        # Vertical Acceleration in metres/second^2
        self.acceleration = 0

        # Current Gravitational Force in Newtons
        self.gravitational_force = 0

        # Current Thrust Force in Newtons
        self.thrust_force = 0

        # Net Force acting on Drone in Newtons
        self.net_force = 0