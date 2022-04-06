#
import datetime
from flight_data import data
from flight_search import get_destinations, get_prices, parse_flight_info

flight_data = data

destination_list = get_destinations()

today_date = datetime.date.today()
six_month = today_date + datetime.timedelta(days=180)

for code in destination_list:
    result = get_prices(f"{code}", today_date.strftime("%d/%m/%Y"), six_month.strftime("%d/%m/%Y"))
# print(result)

parse_flight_info(result)


