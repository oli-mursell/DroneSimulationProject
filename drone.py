""" Contains the Drone class and its data """

import utilities.constants as consts
import utilities.physics as phys

class Drone:
    """
    Represents a quadcopter and its physical properties.

    This class stores:
        1. Physical properties of the drone
        2. Current state of drone during a simulation
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
    def gravitational_force(self):
        """ Returns the gravitational force acting on the drone in Newtons """
        return -self._mass * consts.GRAVITY

    @property
    def acceleration(self):
        """ Returns the current vertical acceleration of the drone in meters/second^2 """
        return phys.calculate_acceleration(self.gravitational_force, self._mass)

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