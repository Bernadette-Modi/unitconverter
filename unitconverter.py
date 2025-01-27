import math
conversion_factors = {
    "length":{
        "mm": 1,
        "cm": 10,
        "m": 1000,
        "km": 1000000,
        "inch": 25.4,
        "ft": 304.8,
        "yd": 914.4,
        "mi": 1609344,
    },
    "weight": {
        "mg": 1,
        "g": 1000,
        "kg": 1000000,
        "oz": 28349.5,
        "ib": 453592,
    },
    "temperature": {
        "celsius": lambda val, to: (val * 9/5 + 32) if to == "fahrenheit" else (val + 273.15),
        "fahrenheit": lambda val, to: ((val - 32)*5/9) if to == "celsius" else ((val - 32)*5/9 + 273.15),
        "kelvin": lambda val, to: (val - 273.15) if to == "celsius" else ((val - 273.15) * 9/5 + 32),
    },
}
def get_conversion_type(unit):
    for conversion_type, units in conversion_factors.items():
        if unit in units:
            return conversion_type
    return None
