# Temperature conversion functions
def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        raise ValueError("Temperature below absolute zero is not allowed.")
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    if fahrenheit < -459.67:
        raise ValueError("Temperature below absolute zero is not allowed.")
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    if celsius < -273.15:
        raise ValueError("Temperature below absolute zero is not allowed.")
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Temperature below absolute zero is not allowed.")
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    if fahrenheit < -459.67:
        raise ValueError("Temperature below absolute zero is not allowed.")
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_fahrenheit(kelvin):
    if kelvin < 0:
        raise ValueError("Temperature below absolute zero is not allowed.")
    return (kelvin * 9/5) - 459.67

# Sample usage
print("25°C to Fahrenheit:", celsius_to_fahrenheit(25))
print("77°F to Celsius:", fahrenheit_to_celsius(77))
print("100°C to Kelvin:", celsius_to_kelvin(100))
print("300 K to Celsius:", kelvin_to_celsius(300))
print("32°F to Kelvin:", fahrenheit_to_kelvin(32))
print("273.15 K to Fahrenheit:", kelvin_to_fahrenheit(273.15))
