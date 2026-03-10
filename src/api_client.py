from abc import ABC, abstractmethod
from typing import Dict, List

import requests

from src.plane_class import Aeroplane


class ApiClient(ABC):
    """Абстрактный класс для работы с API сервисами"""

    @abstractmethod
    def get_aeroplanes(self, keyword: str) -> List[Dict]:
        """Метод для получения данных от сервера"""
        pass


class ApiClientPlanes(ApiClient):
    """Класс для работы с Api запросами"""

    country: str
    openstreetmap_url: str
    opensky_url: str
    aeroplanes: list

    def __init__(self, country=None):
        self.country = country
        self.openstreetmap_url = "https://nominatim.openstreetmap.org/search"
        self.opensky_url = "https://opensky-network.org/api/states/all?"
        self.aeroplanes = []

    def get_aeroplanes(self, key_word: str) -> list[list[str | float]]:
        """Метод для получения данных о самолетах"""
        params_nominatim = {"country": key_word, "format": "json", "limit": 1}
        headers_nominatim = {"User-Agent": "test-app/1.0"}

        # Запрос на получение координат страны
        response = requests.get(url=self.openstreetmap_url, params=params_nominatim, headers=headers_nominatim)
        response.raise_for_status()
        data = response.json()
        self.country = data[0]["name"]
        coordinates = data[0]["boundingbox"]
        params = {"lamin": coordinates[0], "lamax": coordinates[1], "lomin": coordinates[2], "lomax": coordinates[3]}
        response2 = requests.get(url=self.opensky_url, params=params)
        data_plane = response2.json()
        data_plane = data_plane["states"]
        print(len(data_plane))
        data_plane_new = []
        for plan in data_plane:
            param_plane = [plan[0], plan[2], plan[9], plan[10], plan[13]]
            data_plane_new.append(param_plane)
        self.aeroplanes = data_plane_new
        return data_plane_new

    @staticmethod
    def convert_to_aeroplanes(data_plane_new: list[list[str | float]]) -> List[Aeroplane]:
        """Метод для получения данных о самолетах в виде объектов Aeroplane"""
        list_aeroplane = []
        for plan in data_plane_new:
            p = Aeroplane(
                icao24=plan[0], origin_country=plan[1], velocity=plan[2], geo_altitude=plan[3], true_track=plan[4]
            )
            list_aeroplane.append(p)
        return list_aeroplane
