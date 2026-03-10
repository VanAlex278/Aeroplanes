from unittest.mock import patch
import pytest
from src.api_client import ApiClientPlanes
from src.plane_class import Aeroplane


@pytest.fixture
def api_client():
    return ApiClientPlanes()


def test_init(api_client):
    """Тест инициализации клиента"""
    assert api_client.country is None
    assert api_client.openstreetmap_url == 'https://nominatim.openstreetmap.org/search'
    assert api_client.opensky_url == 'https://opensky-network.org/api/states/all?'
    assert api_client.aeroplanes == []


@patch('requests.get')
def test_get_aeroplanes(mock_get, api_client):
    """Тест успешного получения данных о самолетах"""

    mock_get.return_value.json.return_value = {
        0: {"name": "Canada", "boundingbox": ["41", "83", "-14", "57"]},
        "states":  [["4b1812", "SWR", "Canada", 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
        }

    result = api_client.get_aeroplanes("Canada")

    assert result == [["4b1812", "Canada", 9, 10, 13]]


def test_convert_to_aeroplanes():
    """Тест преобразования данных в объекты Aeroplane"""
    data_list = [
        ['8a02cb', 'Indonesia', 118.57, 145.97, 2293.62],
        ['8a03b2', 'Indonesia', 71.84, 68.58, 358.14],
        ['8a0363', 'Indonesia', 221.33, 91.86, 10271.76],
        ['781a7a', 'China', 244.34, 174.81, 10401.3],
        ['8a04f5', 'Indonesia', 150.81, 108.5, 2834.64],
        ['8a04e4', 'Indonesia', 230.1, 92.05, 12001.5]
    ]

    list_planes = ApiClientPlanes.convert_to_aeroplanes(data_list)

    assert len(list_planes) == 6
    assert isinstance(list_planes[0], Aeroplane)
    assert list_planes[0].icao24 == '8a02cb'
    assert list_planes[0].origin_country == 'Indonesia'
