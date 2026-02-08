EMISSION_FACTORS = {
    "HFO": 0.0132,
    "MDO": 0.0132,
    "LNG": 0.010,
    "Biofuel": 0.005
}

def calculate_co2(row):
    fuel = row["fuel_type"]

    if fuel not in EMISSION_FACTORS:
        raise ValueError(f"Unbekannter Treibstoff: {fuel}")

    factor = EMISSION_FACTORS[fuel]

    co2 = row["distance_km"] * row["containers"] * factor
    return co2
