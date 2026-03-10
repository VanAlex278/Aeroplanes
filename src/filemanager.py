import os
import json

from src.api_client import ApiClientPlanes


class JSONAeroplane:
    """Класс для работы с JSON-файлами"""

    def __init__(self, filename: str = "data/aeroplane.json"):
        self.__file_name = filename
        self._file_exists()

    def _file_exists(self) -> None:
        """Создает файл, если он не существует"""

        if not os.path.exists(self.__file_name):
            with open(self.__file_name, 'w', encoding='utf-8') as json_file:
                json.dump([], json_file, ensure_ascii=False, indent=2)

    def get_planes(self) -> list:
        """Чтение данных о самолетах из файла"""

        try:
            with open(self.__file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
        except json.JSONDecodeError:
            return []

    def write_planes(self, planes) -> None:
        """Запись данных о самолетах в файл"""

        with open(self.__file_name, 'w', encoding='utf-8') as f:
            json.dump(planes, f, ensure_ascii=False, indent=2)

    def clear_all(self) -> None:
        """Очистка всего JSON-файла"""

        self.write_planes([])
