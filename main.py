version = str('0.0.1')

print('Ubertool', version, 'initialized')

fallback_miles_per_gallon = 28.6    # defaults to 28.6 if left blank, derived from 2019 330i mpg
fallback_gas_cost_per_gallon = 4.619  # default if left blank, derived from cost of costco 87

def find_gas_consumed(miles_per_gallon, trip_distance):
    if miles_per_gallon is None:
        miles_per_gallon = fallback_miles_per_gallon 
    gas_consumed = trip_distance / miles_per_gallon
    return gas_consumed

def find_gas_cost(gas_consumed, gas_cost_per_gallon):
    if gas_cost_per_gallon is None:
        gas_cost_per_gallon = fallback_gas_cost_per_gallon
    gas_cost = gas_consumed * gas_cost_per_gallon
    return gas_cost

def find_net_profit(gas_cost, trip_revenue):
    net_profit = trip_revenue - gas_cost
    return net_profit

while True:
    trip_revenue = float(input('Please enter total trip revenue: '))
    trip_distance = float(input('Please enter trip distance in miles: '))
    miles_per_gallon = float(input('Please enter car fuel economy in MPG (default if blank: ' + str(fallback_miles_per_gallon) + '): '))
    gas_cost_per_gallon = float(input('Please enter gas cost per gallon (default if blank: ' + str(fallback_gas_cost_per_gallon) + '): '))

    gas_consumed = find_gas_consumed(miles_per_gallon, trip_distance)
    print('Calculated gas consumed:', round(gas_consumed, 2), 'gallons')

    gas_cost = find_gas_cost(gas_consumed, gas_cost_per_gallon)
    print('Calculated cost of gas consumed:', '$' + str(round(gas_cost, 2)))

    print('\n' + '\n' + '\n')
    net_profit = find_net_profit(gas_cost, trip_revenue)
    print('Calculated net profit:', '$' + str(round(net_profit, 2)))