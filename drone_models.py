""" Contains different drone models and their properties """
from drone import Drone

class Skydiox10D(Drone):
    """
    Represents the Skydiox 10D drone model and its physical properties.
    
    This class stores:
        1. Physical properties of the Skydiox 10D drone
        2. Current state of the drone during a simulation
    """
    def __init__(self,
                initial_position=0,
                initial_velocity=0):

        super().__init__(
            mass=2.11,
            name="Skydiox 10D",
            overall_length=0.790,
            overall_width=0.650,
            overall_height=0.145,
            initial_position=initial_position,
            initial_velocity=initial_velocity
            )