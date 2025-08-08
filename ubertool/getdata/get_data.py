"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the ubertool project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""

from config.settings import *

def get_user_values():
    trip_revenue = str(input('Please enter total trip revenue: ')).strip()
    trip_distance = str(input('Please enter trip distance in miles: ')).strip()
    miles_per_gallon = str(input('Please enter car fuel economy in MPG (default if blank: ' + str(gas_settings['default_car_miles_per_gallon']) + '): ')).strip()
    gas_cost_per_gallon = str(input('Please enter gas cost per gallon (default if blank: ' + str(gas_settings['default_price_gas_per_gallon']) + '): ')).strip()
    
    # ERROR HANDLING
    try:
        trip_revenue = float(trip_revenue) if trip_revenue else 0
    except:
        trip_revenue = 0

    try:
        trip_distance = float(trip_distance) if trip_distance else 0
    except:
        trip_distance = 0

    try:
        miles_per_gallon = float(miles_per_gallon) if miles_per_gallon else gas_settings['default_car_miles_per_gallon']
    except:
        miles_per_gallon = gas_settings['default_car_miles_per_gallon']

    try:
        gas_cost_per_gallon = float(gas_cost_per_gallon) if gas_cost_per_gallon else gas_settings['default_price_gas_per_gallon']
    except:
        gas_cost_per_gallon = gas_settings['default_price_gas_per_gallon']
    
    
    return trip_revenue, trip_distance, miles_per_gallon, gas_cost_per_gallon