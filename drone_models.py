""" Contains different drone models and their properties """
from drone import Drone
from motors import Motor

class HolybroX650(Drone):
    """
    Represents the Holybro X650 drone model and its physical properties.
    
    This class stores:
        1. Physical properties of the Holybro X650 drone
        2. Current state of the drone during a simulation
    """
    def __init__(self,
                initial_position=0,
                initial_velocity=0):

        # X650 Quadcopter Specifications
        motors = [
            Motor(max_thrust=15),  # Motor 1
            Motor(max_thrust=15),  # Motor 2
            Motor(max_thrust=15),  # Motor 3
            Motor(max_thrust=15)   # Motor 4
        ]

        super().__init__(
            mass=2.00,
            name="Holybro X650",
            overall_length=0.460,
            overall_width=0.460,
            overall_height=0.398,
            initial_position=initial_position,
            initial_velocity=initial_velocity,
            motors=motors
            )