import numpy as np

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

vectorized_convert = np.vectorize(fahrenheit_to_celsius)

fahrenheit_temps = np.array([32, 68, 100, 212, 77])

celsius_temps = vectorized_convert(fahrenheit_temps)
print(celsius_temps)