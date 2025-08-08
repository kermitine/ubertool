"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the DHOC project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""

version = '0.1.2'
trip = 1
import time
from KermLib.KermLib import *


KermLib.ascii_run()
print('Ubertool', version, 'initialized')
print('\n' * 3)

fallback_miles_per_gallon = 28.6    # defaults to 28.6 if left blank, derived from 2019 330i mpg
fallback_gas_cost_per_gallon = 4.619  # default if left blank, derived from cost of costco 87

def find_gas_consumed(miles_per_gallon, trip_distance):
    gas_consumed = trip_distance / miles_per_gallon
    return gas_consumed

def find_gas_cost(gas_consumed, gas_cost_per_gallon):
    gas_cost = gas_consumed * gas_cost_per_gallon
    return gas_cost

def find_net_profit(gas_cost, trip_revenue):
    net_profit = trip_revenue - gas_cost
    return net_profit

def get_user_values():
    trip_revenue = str(input('Please enter total trip revenue: ')).strip()
    trip_distance = str(input('Please enter trip distance in miles: ')).strip()
    miles_per_gallon = str(input('Please enter car fuel economy in MPG (default if blank: ' + str(fallback_miles_per_gallon) + '): ')).strip()
    gas_cost_per_gallon = str(input('Please enter gas cost per gallon (default if blank: ' + str(fallback_gas_cost_per_gallon) + '): ')).strip()
    
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
        miles_per_gallon = float(miles_per_gallon) if miles_per_gallon else fallback_miles_per_gallon
    except:
        miles_per_gallon = fallback_miles_per_gallon

    try:
        gas_cost_per_gallon = float(gas_cost_per_gallon) if gas_cost_per_gallon else fallback_gas_cost_per_gallon
    except:
        gas_cost_per_gallon = fallback_gas_cost_per_gallon
    
    
    return trip_revenue, trip_distance, miles_per_gallon, gas_cost_per_gallon

def calculate_values(trip_revenue, trip_distance, miles_per_gallon, gas_cost_per_gallon):
    print('\n' * 3)

    gas_consumed = find_gas_consumed(miles_per_gallon, trip_distance)
    print('Calculated gas consumed:', round(gas_consumed, 2), 'gallons')

    gas_cost = find_gas_cost(gas_consumed, gas_cost_per_gallon)
    print('Calculated cost of gas consumed:', '$' + str(round(gas_cost, 2)))

    net_profit = find_net_profit(gas_cost, trip_revenue)
    print('Calculated net profit:', '$' + str(round(net_profit, 2)))

    return net_profit

# PROGRAM LOOP

while True:
    print("Trip " + '#' + str(trip) + ':')
    trip += 1
    trip_revenue, trip_distance, miles_per_gallon, gas_cost_per_gallon = get_user_values()
    calculate_values(trip_revenue, trip_distance, miles_per_gallon, gas_cost_per_gallon)
    time.sleep(2)

    print('Would you like to calculate another trip? (y/n)?')
    cont = KermLib.get_user_input(['y', 'Y', 'n', 'N'])
    if cont not in ['y', 'Y']:
        break
    print('\n' * 3)
