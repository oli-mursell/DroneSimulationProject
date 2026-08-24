""" Contains different drone models and their properties """
from drone import Drone
from motors import Motor
from motor_data import X650_MOTOR_DATA

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

        motors = [
            Motor(
                max_rpm=X650_MOTOR_DATA["max_rpm"],
                throttle_data=X650_MOTOR_DATA["throttle"],
                rpm_data=X650_MOTOR_DATA["rpm"],
                thrust_data=X650_MOTOR_DATA["thrust"],
                torque_data=X650_MOTOR_DATA["torque"]
            ) 
            for _ in range(4)
        ]

        super().__init__(
            mass=3.10,
            name="Holybro X650",
            overall_length=0.460,
            overall_width=0.460,
            overall_height=0.398,
            initial_position=initial_position,
            initial_velocity=initial_velocity,
            motors=motors
            )