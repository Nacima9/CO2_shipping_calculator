"""
Berechnet den gesamten CO₂-Ausstoß pro Jahr.
"""
def calculate_total_co2_per_year(rows):
    totals = {}

    for row in rows:
        year = row["year"]
        co2 = row["co2_kg"]

        if year not in totals:
            totals[year] = 0.0

        totals[year] += co2

    return totals

"""
Berechnet den durchschnittlichen CO₂-Ausstoß pro Transport und Jahr.
"""
def calculate_average_co2_per_year(rows):
    sums = {}
    counts = {}

    for row in rows:
        year = row["year"]
        co2 = row["co2_kg"]

        if year not in sums:
            sums[year] = 0.0
            counts[year] = 0

        sums[year] += co2
        counts[year] += 1

    averages = {}
    for year in sums:
        averages[year] = sums[year] / counts[year]

    return averages
