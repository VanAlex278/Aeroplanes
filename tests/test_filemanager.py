from src.filemanager import JSONAeroplane


def test_init_json():
    """Тест инициализации клиента"""
    file_name = "data/aeroplane.json"
    list_planes1 = JSONAeroplane(file_name)
    # assert list_planes1.__file_name == ""
