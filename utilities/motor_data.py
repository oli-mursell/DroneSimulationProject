""" Contains motor performance data for various motors used """

# Holybro X650 Motor Data
#
# Motor: T-Motor MN4014 KV330
#
# Propeller: T-Motor 15x5CF
#
# Battery: 6S LiPo (22.2V)
#
# Thrust has been converted from grams-force to Newtons (1 g-force = 0.00981 N)
# 
# Torque has been calculated from published power and RPM: 
#   torque = power / angular_velocity, where: angular_velocity = 2 * pi * RPM / 60


X650_MOTOR_DATA = {
    "max_rpm": 6000,

    "throttle": [
        0.00,
        0.50,
        0.65,
        0.75,
        0.85,
        1.00
    ],

    "rpm": [
        0,
        3900,
        4600,
        5100,
        5600,
        6000
    ],

    "thrust": [
        0.0,
        8.142,
        11.282,
        14.028,
        16.579,
        18.835
    ],

    "torque": [
        0.0,
        0.198,
        0.272,
        0.324,
        0.382,
        0.420
    ]
}
