""" Contains the Drone class and its data """

class Drone:
    """
    Represents a quadcopter and its physical properties.

    This class stores:
        1. Physical properties of the drone
        2. Current state of drone during a simulation
    """
    def __init__(self):
        
        # Mass of the drone in kg - with Connect SL
        self.mass = 2.11

        # Identifying name of the drone
        self.name = "Skydio X10D"

        # Physical dimensions of the unfolded drone in meters
        self.overall_length = 0.790
        self.overall_width = 0.650
        self.overall_height = 0.145

        # Vertical Position in metres
        self.position = 0

        # Vertical Velocity in metres/second
        self.velocity = 0

        # Vertical Acceleration in metres/second^2
        self.acceleration = 0

        # Current Gravitational Force in Newtons
        self.gravitational_force = 0

        # Net Force acting on Drone in Newtons
        self.net_force = 0