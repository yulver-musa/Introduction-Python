from numb3rs import validate


def test_valid_ipv4():
    assert validate("192.168.1.1")
    assert validate("0.0.0.0")
    assert validate("255.255.255.255")


def test_invalid_range():
    assert not validate("275.3.6.28")
    assert not validate("256.256.256.256")
    assert not validate("192.168.1.999")


def test_invalid_format():
    assert not validate("192.168.1")
    assert not validate("192.168.1.1.1")
    assert not validate("cat.3.6.28")
    assert not validate("192.168.one.1")


def test_leading_zeros():
    assert not validate("01.2.3.4")
    assert not validate("192.168.001.1")
    assert not validate("00.0.0.0")
