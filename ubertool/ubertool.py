"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the DHOC project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""

from ubertool.getdata.get_data import *
from ubertool.computation.computation import *
from utils.KermLib.KermLib import KermLib
from config.settings import *

KermLib.ascii_run()
print('Ubertool', version, 'initialized')
print('\n' * 3)

while True: # MAIN LOOP
    print("Trip " + '#' + str(trip) + ':')
    trip += 1
    trip_revenue, trip_distance, miles_per_gallon, gas_cost_per_gallon = get_user_values()
    calculate_values(trip_revenue, trip_distance, miles_per_gallon, gas_cost_per_gallon)

    print('Would you like to calculate another trip? (y/n)?')
    cont = KermLib.get_user_input(['y', 'Y', 'n', 'N'])
    if cont not in ['y', 'Y']:
        break
    print('\n' * 3)
