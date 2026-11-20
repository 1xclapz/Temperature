def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def get_colour(celsius):
    # blue = cold, green = mild, orange = hot
    if celsius < 10:
        return "#4da6ff"
    elif celsius < 25:
        return "#5cd65c"
    else:
        return "#ff9933"


def format_temp(celsius, unit):
    if unit == "C":
        return f"{celsius:.0f}°C"
    return f"{to_fahrenheit(celsius):.0f}°F"