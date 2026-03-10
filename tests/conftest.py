import pytest

from src.plane_class import Aeroplane


@pytest.fixture
def test_plane1():
    return Aeroplane('71c535', 'Republic of Korea', 207.27, 301.91, 8115.3)


@pytest.fixture
def test_plane2():
    return Aeroplane('8514b4', 'Japan', 102.84, 49.06, 1074.42)


# @pytest.fixture
# def test_planes_list():
#     return [
#         ['71c535', 'Republic of Korea', 207.27, 301.91, 8115.3],
#         ['8514b4', 'Japan', 102.84, 49.06, 1074.42],
#         ['8a0363', 'Indonesia', 221.33, 91.86, 10271.76],
#         ['781a7a', 'China', 244.34, 174.81, 10401.3],
#         ['8a04f5', 'Indonesia', 150.81, 108.5, 2834.64],
#         ['8a04e4', 'Indonesia', 230.1, 92.05, 12001.5]
#     ]


