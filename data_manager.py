import requests

BEARER_HEADERS = {"Authorization": "Bearer trapamagicrrr"}
API_URL = "https://api.sheety.co/2e1344f81aaa5a449d9cbb89d1818cc3/flightDeals/prices"


def get_sheet():
    sheet = requests.get(url=API_URL, headers=BEARER_HEADERS)
    return sheet


def get_rows(row):
    row = requests.get(url=f"{API_URL}/{row}", headers=BEARER_HEADERS)
    return row.json()


def edit_IATA(replacement, row):
    requests.put(url=f"{API_URL}/{row}", json=replacement, headers=BEARER_HEADERS)

def iata_update():
    pass
    for rows in range(2, 10):
        row = get_rows(rows)
        city = row['price']['city']
        iata_code = location_pull(city)
        row['price'].update({'iataCode': f'{iata_code}'})
        edit_IATA(row, rows)


# def put_IATA():
##TODO Merge with flight_search api
#     put_request = requests.put(url= API_URL, headers=BEARER_HEADERS)
#     for entry in flight_data['prices']:
#         location = entry['city']
#         location_pull(location)
#     pass

class DataManager:
    pass
