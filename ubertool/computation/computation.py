"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the DHOC project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""

def find_gas_consumed(miles_per_gallon, trip_distance):
    gas_consumed = trip_distance / miles_per_gallon
    return gas_consumed

def find_gas_cost(gas_consumed, gas_cost_per_gallon):
    gas_cost = gas_consumed * gas_cost_per_gallon
    return gas_cost

def find_net_profit(gas_cost, trip_revenue):
    net_profit = trip_revenue - gas_cost
    return net_profit


def calculate_values(trip_revenue, trip_distance, miles_per_gallon, gas_cost_per_gallon):
    print('\n' * 3)

    gas_consumed = find_gas_consumed(miles_per_gallon, trip_distance)
    print('Calculated gas consumed:', round(gas_consumed, 2), 'gallons')

    gas_cost = find_gas_cost(gas_consumed, gas_cost_per_gallon)
    print('Calculated cost of gas consumed:', '$' + str(round(gas_cost, 2)))

    net_profit = find_net_profit(gas_cost, trip_revenue)
    print('Calculated net profit:', '$' + str(round(net_profit, 2)))

    return net_profit