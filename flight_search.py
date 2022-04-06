import requests
from flight_data import data

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "xMX9gy4oGe5b2uwftErwDHGSJ1H-yLAm"
flight_list = []


def location_pull(location):
    location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
    kiwi_header = {"apikey": TEQUILA_API_KEY}
    query = {"term": f"{location}", "location_types": "city"}
    response = requests.get(url=location_endpoint, headers=kiwi_header, params=query)
    response.raise_for_status()
    results = response.json()["locations"]
    return results[0]['code']


def get_destinations():
    # Pull the destinations from local dict, would be google sheet or DB if live
    d_list = []
    for entry in data['prices']:
        d_list.append(entry['iataCode'])
    return d_list


def get_prices(iata_code, today, date_out):
    # Get a list of flights to an iataCode under a set pricepoint
    price_endpoint = f"{TEQUILA_ENDPOINT}/search"
    kiwi_header = {"apikey": TEQUILA_API_KEY}
    search = {"fly_from": "NYC", "fly_to": f"{iata_code}", "date_from": f"{today}", "date_to": f"{date_out}",
              "curr": 'USD'}
    response = requests.get(url=price_endpoint, headers=kiwi_header, params=search)
    response = response.json()
    global flight_list
    print(len(response['data']))
    for entry in response['data']:
        if entry['price'] < 300:
            flight_list.append(entry)
    return flight_list


def parse_flight_info(flights):
    # Take the picked flights and output the relevant information
    # relevant_keys = ['flyFrom', 'flyTo', 'cityFrom', 'cityTo', 'price']
    # relevant_result  #If data were to be parsed and delivered it would be picked out and saved here
    print("Here are the relevant flights in a list:")
    for entry in flights:
        print(f"{entry['flyFrom']} {entry['cityFrom']} to {entry['flyTo']} {entry['cityTo']} for ${entry['price']}")
