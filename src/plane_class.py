class Aeroplane:
    """Класс самолеты"""

    icao24: str  # уникальный идентификатор борта
    origin_country: str  # страна регистрации
    velocity: float  # скорость
    geo_altitude: float  # высота
    true_track: float  # курс
    # list_planes = [] # количество самолетов

    __slots__ = ("icao24", "origin_country", "velocity", "geo_altitude", "true_track")

    def __init__(self, icao24, origin_country, velocity, geo_altitude, true_track=0.0):
        self.icao24 = icao24
        self.origin_country = origin_country
        self.velocity = velocity
        self.geo_altitude = self.__validate_geo_altitude(geo_altitude)
        self.true_track = true_track
        # Aeroplane.list_planes.append([self.icao24, self.origin_country, self.velocity, self.geo_altitude, self.true_track])


    @staticmethod
    def __validate_geo_altitude(geo_altitude):
        """Приватный метод валидации высоты полета"""
        if geo_altitude < 0:
            geo_altitude = 0
        return geo_altitude


    def __str__(self):
        return (
            f"Уникальный идентификатор борта: {self.icao24}. "
            f"Страна регистрации: {self.origin_country}. "
            f"Скорость: {self.velocity}. "
            f"Высота полета: {self.geo_altitude}. "
            f"Курс: {self.true_track}."
        )


    def __eq__(self, other: object) -> bool:
        """Проверка на равенство по высоте полета"""

        if not isinstance(other, Aeroplane):
            return False
        return self.geo_altitude == other.geo_altitude

    def __lt__(self, other: object) -> bool:
        """Проверка на меньше по высоте полета"""

        if not isinstance(other, Aeroplane):
            return NotImplemented
        return self.geo_altitude < other.geo_altitude

    def __le__(self, other: object) -> bool:
        """Проверка на меньше или равно по высоте полета"""

        if not isinstance(other, Aeroplane):
            return NotImplemented
        return self.geo_altitude <= other.geo_altitude

    def __gt__(self, other: object) -> bool:
        """Проверка на больше по высоте полета"""

        if not isinstance(other, Aeroplane):
            return NotImplemented
        return self.geo_altitude > other.geo_altitude

    def __ge__(self, other: object) -> bool:
        """Проверка на больше или равно по высоте полета"""

        if not isinstance(other, Aeroplane):
            return NotImplemented
        return self.geo_altitude >= other.geo_altitude



    def to_list(self) -> list:
        """Возвращает список данных о самолетах"""

        return [self.icao24, self.origin_country, self.velocity, self.geo_altitude, self.true_track]
