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
            max_rpm,
            throttle_data,
            rpm_data,
            thrust_data,
            torque_data,
            current_throttle=0,
            ):

        # Maximum RPM of the motor
        self._max_rpm = max_rpm

        # Motor performance data
        self._throttle_data = throttle_data
        self._rpm_data = rpm_data
        self._thrust_data = thrust_data
        self._torque_data = torque_data

        # Current state of the motor
        self._current_throttle = current_throttle
        self._current_rpm = 0
        self._current_thrust = 0
        self._current_torque = 0

        self.set_throttle_and_rpm(current_throttle, 0)

    @property
    def throttle(self):
        """ Returns the current throttle between 0 and 1 """
        return self._current_throttle

    @property
    def current_rpm(self):
        """ Returns the current RPM of the motor """
        return self._current_rpm

    @property
    def current_thrust(self):
        """ Returns the current thrust of the motor in Newtons """
        return self._current_thrust

    @property
    def current_torque(self):
        """ Returns the current torque of the motor in Newton-meters """
        return self._current_torque

    def set_throttle_and_rpm(self, throttle, rpm):
        """ Sets the current throttle and RPM as values between 0 and 1

        Updating throttle also updates the RPM, thrust and torque 
        """
        
        throttle = max(0, min(throttle, 1))
        rpm = max(0, min(rpm, 1))

        self._current_throttle = throttle
        self._current_rpm = rpm

        self._current_rpm = self._interpolate(
            throttle, 
            self._throttle_data, 
            self._rpm_data
            )

        self._current_throttle = self._interpolate(
            rpm, 
            self._rpm_data, 
            self._throttle_data
            )

        self._current_thrust = self._calculate_thrust(self._current_rpm)

        self._current_torque = self._calculate_torque(self._current_rpm)

    def _calculate_thrust(self, rpm):
        """ Calculates the thrust of the motor based on the current RPM """
        return self._interpolate(rpm, self._rpm_data, self._thrust_data)

    def _calculate_torque(self, rpm):
        """ Calculates the torque of the motor based on the current RPM """
        return self._interpolate(rpm, self._rpm_data, self._torque_data)

    def _calculate_rpm(self, throttle):
        """ Calculates the RPM of the motor based on the current throttle """
        return self._interpolate(throttle, self._throttle_data, self._rpm_data)

    @staticmethod
    def _interpolate(value, x_data, y_data):
        """ Linearly interpolates the y value for a given x value

        Args:
            value: The x value for which to interpolate
            x_data: List of x values
            y_data: List of y values
        Returns:
            float: The interpolated y value for the given x value
        """

        if len(x_data) != len(y_data):
            raise ValueError("x_data and y_data must have the same length")

        if len(x_data) < 2:
            raise ValueError("At least 2 data points are required for interpolation")

        if value <= x_data[0]:
            return y_data[0]
        
        if value >= x_data[-1]:
            return y_data[-1]

        for i in range(len(x_data) - 1):

            x1 = x_data[i]
            x2 = x_data[i + 1]

            if x1 <= value <= x2:
                # Linear interpolation formula

                y1 = y_data[i]
                y2 = y_data[i + 1]

                return y1 + (y2 - y1) * (value - x1) / (x2 - x1)

        raise ValueError("Value is out of bounds")