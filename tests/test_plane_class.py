def test_init_plane(capsys, test_plane1):
    assert test_plane1.icao24 == "71c535"
    assert test_plane1.origin_country == "Republic of Korea"
    assert test_plane1.velocity == 207.27
    assert test_plane1.geo_altitude == 301.91
    assert test_plane1.true_track == 8115.3
    # assert test_plane1.list_planes == [["71c535", "Republic of Korea", 207.27, 301.91, 8115.3]]
    print(test_plane1)
    message = capsys.readouterr()
    assert message.out.strip() == ('Уникальный идентификатор борта: 71c535. Страна регистрации: '
                                   'Republic of Korea. Скорость: 207.27. Высота полета: 301.91. Курс: 8115.3.')


def test_compare_planes(test_plane1, test_plane2):
    assert test_plane1 > test_plane2


def test_to_list(test_plane1):
    assert test_plane1.to_list() == ["71c535", "Republic of Korea", 207.27, 301.91, 8115.3]
