# d04_debug.py

import math
signal_power = 9
noise_power  = 10
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print decibels


