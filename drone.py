""" Contains the Drone class """

from abc import ABC
import utilities.constants as consts
import utilities.physics as phys

# Abstract class for a drone
class Drone(ABC):
    """
    Represents a quadcopter and its physical properties.

    This class stores:
        1. Physical properties of the drone
        2. Current state of drone during a simulation
        3. Motors on the drone and their properties
    """
    def __init__(
            self, 
            name=None, 
            mass=None,
            overall_length=None,
            overall_width=None,
            overall_height=None, 
            initial_position=0, 
            initial_velocity=0,
            motors=None 
            ):
        
        # Mass of the drone in kg 
        self._mass = mass

        # Identifying name of the drone
        self._name = name

        # Physical dimensions of the unfolded drone in meters
        self._overall_length = overall_length   
        self._overall_width = overall_width
        self._overall_height = overall_height

        # Vertical Position in metres
        self._position = initial_position

        # Vertical Velocity in metres/second
        self._velocity = initial_velocity

        # List of motors on the drone
        self._motors = motors if motors is not None else []

    @property
    def mass(self):
        """ Returns the mass of the drone in kg """
        return self._mass

    @property
    def name(self):
        """ Returns the name of the drone """
        return self._name

    @property
    def overall_length(self):
        """ Returns the overall length of the drone in meters """
        return self._overall_length

    @property
    def overall_width(self):
        """ Returns the overall width of the drone in meters """
        return self._overall_width

    @property
    def overall_height(self):
        """ Returns the overall height of the drone in meters """
        return self._overall_height

    @property
    def motors(self):
        """ Returns the list of motors on the drone """
        return self._motors

    @property
    def total_thrust(self):
        """ Returns the total thrust produced by all motors in Newtons """
        return sum(motor.current_thrust for motor in self._motors)

    @property
    def total_torque(self):
        """ Returns the total torque produced by all motors in Newton-meters """
        return sum(motor.current_torque for motor in self._motors)

    @property
    def gravitational_force(self):
        """ Returns the gravitational force acting on the drone in Newtons """
        return -self._mass * consts.GRAVITY

    @property
    def net_force(self):
        """ Returns the net force acting on the drone in Newtons """
        return phys.net_forces([self.gravitational_force, self.total_thrust])

    @property
    def acceleration(self):
        """ Returns the current vertical acceleration of the drone in meters/second^2 """
        return phys.calculate_acceleration(self.net_force, self._mass)

    def set_motor_throttles(self, throttles):
        """ Sets the throttles of the motors on the drone """
        if len(throttles) != len(self._motors):
            raise ValueError("Number of throttles must match number of motors.")
        for motor, throttle in zip(self._motors, throttles):
            motor.set_throttle(throttle)

    def update_status(self):
        """ Updates the drone's position and velocity based on its acceleration and the time step """
        self._position = phys.update_position(
            self._position, 
            self._velocity, 
            consts.TIMESTEP)

        self._velocity = phys.update_velocity(
            self._velocity,
            self.acceleration,
            consts.TIMESTEP)

    def get_status(self):
        """ Returns the current position and velocity of the drone """
        return self._position, self._velocity