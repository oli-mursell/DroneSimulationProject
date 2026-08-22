""" Contains the Motor class"""

class Motor:
    """
    Represents a motor and its thrusts.

    This class stores:
        1. Physical properties of the motor
        2. Current state of the motor during a simulation
    """
    def __init__(
            self, 
            max_thrust=None,
            current_thrust=0,
            ):
        
        # Maximum thrust of the motor in Newtons
        self._max_thrust = max_thrust

        # Current thrust of the motor in Newtons
        self._current_thrust = current_thrust

    @property
    def max_thrust(self):
        """ Returns the maximum thrust of the motor in Newtons """
        return self._max_thrust

    @property
    def current_thrust(self):
        """ Returns the current thrust of the motor in Newtons """
        return self._current_thrust

    @property
    def throttle(self):
        """ Returns the current throttle percentage of the motor """
        if not self ._max_thrust:
            return 0
        return (self._current_thrust / self._max_thrust)

    def set_thrust(self, thrust):
        """ Sets the current thrust of the motor in Newtons """
        if thrust < 0:
            thrust = 0
        if thrust > self._max_thrust and self._max_thrust is not None:
            thrust = self._max_thrust
        self._current_thrust = thrust

    def set_throttle(self, throttle):
        """ Sets the current throttle percentage of the motor """
        if self._max_thrust is None:
            raise ValueError("Max thrust must be set before setting throttle.")
        throttle = max(0, min(throttle, 1))
        self._current_thrust = throttle * self._max_thrust