import os

import requests


def country_api(country):
    openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
    params_nominatim = {
        'country': country,
        'format': 'json',
        'limit': 1,
    }
    headers_nominatim = {
        'User-Agent': 'test-app/1.0',
    }
    response = requests.get(url=openstreetmap_url, params=params_nominatim, headers=headers_nominatim)

    data = response.json()
    coordinates = data[0]['boundingbox']
    return coordinates


def get_plane(boundingbox):
    opensky_url = 'https://opensky-network.org/api/states/all?'
    geo_coordinates = boundingbox
    params = {
        'lamin': geo_coordinates[0],
        'lamax': geo_coordinates[1],
        'lomin': geo_coordinates[2],
        'lomax': geo_coordinates[3],
    }
    response = requests.get(url=opensky_url, params=params)
    # data = response.status_code
    data = response.json()
    return data




if __name__ == "__main__":
    koord = country_api("Indonesia") # ['-11.2085669', '6.2744496', '94.7717124', '141.0194444']
    print(koord)
    print(get_plane(koord))
