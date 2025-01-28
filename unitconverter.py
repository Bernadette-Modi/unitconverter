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

def convert_units(value, from_unit, to_unit):
    from_type = get_conversion_type(from_unit)
    to_type = get_conversion_type(to_unit)
    if from_type != to_type:
        raise ValueError("Conversion between different types is not supported.")
    if from_type == "temperature":
        return conversion_factors[from_type][from_unit](value, to_unit)
    base_value = value * conversion_factors[from_type][from_unit]
    return base_value / conversion_factors[from_type][to_unit]

def main():
    print("Welcome to the Unit Converter!")
    print("You can convert between units of Length, Weight, and Temperature.")

    while True:
        try:
            print("\nSelect a measurement type to convert: ")
            print("1. Length")
            print("2. Weight")
            print("3. Temperature")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")
            if choice == "4":
                print("Thank you for using the Unit Converter. Goodbye!")
                break 
            if choice not in ["1", "2", "3"]:
                print("Invalid choice. Please try again.")
                continue
            measurement_type = ["length", "weight", "temperature"][int(choice)-1]
            print(f"\nAvailable units for {measurement_type.capitalize()}: {', '.join(conversion_factors[measurement_type].keys())}")

            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the unit to convert from: ").lower()
            to_unit = input("Enter the unit to convert to: ").lower()

            if from_unit not in conversion_factors[measurement_type] or to_unit not in conversion_factors[measurement_type]:
                print("Invalid units for the selected measurement type. Please try again.")
                continue
            
            result = convert_units(value, from_unit, to_unit)
            print(f"Converted value: {result: .2f} {to_unit}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occured: {e}")
if __name__ == "__main__":
    main()
