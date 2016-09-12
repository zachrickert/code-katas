# -*- coding: utf-8 -*-
import pytest

from flight_paths import DATA_URL

TEST_JSON = '''[{"city": "Goma", "destination_airports": ["N'djili Airport", "Bangoka International Airport", "Addis Ababa Bole International Airport"], "airport": "Goma International Airport", "lat_lon": [-1.669889, 29.238278]}, {"city": "Kinshasa", "destination_airports": ["Goma International Airport", "Bangoka International Airport", "Lubumbashi International Airport", "Maya-Maya Airport", "Jomo Kenyatta International Airport", "Mohammed V International Airport", "Quatro de Fevereiro Airport", "OR Tambo International Airport", "Port Bouet Airport", "Test Airport"], "airport": "N'djili Airport", "lat_lon": [-4.38575, 15.4445694]},{"city": "Test", "destination_airports": ["Goma International Airport", "Bangoka International Airport", "Lubumbashi International Airport", "Maya-Maya Airport", "Jomo Kenyatta International Airport", "Mohammed V International Airport", "Quatro de Fevereiro Airport", "OR Tambo International Airport", "Port Bouet Airport"], "airport": "Test Airport", "lat_lon": [-4.38575, 15.4445694]}]'''

def test_read_file():
    """Test to see if expected data is in file read."""
    from flight_paths import read_file
    data = read_file(DATA_URL)
    assert 'Goma' in data


def test_read_file_end_of_file():
    """
    Test to see if expected data is in file read.
    Something near the end to check if all data being read.
    """
    from flight_paths import read_file
    data = read_file(DATA_URL)
    assert '-176.1992278' in data


def test_parse_json():
    """Test to see if json is importing correctly."""
    from flight_paths import parse_json
    json_data = parse_json(TEST_JSON)
    assert json_data[0]['airport'] == 'Goma International Airport'


def test_airport_lookup():
    """Test to see if airport lookup function is working correctly."""
    from flight_paths import airport_lookup, parse_json
    airport_dict = airport_lookup(parse_json(TEST_JSON), "N'djili Airport")
    assert airport_dict['city'] == 'Kinshasa'


def test_airport_lookup_not_in_data():
    """Test to see if airport lookup function is working correctly."""
    from flight_paths import airport_lookup, parse_json
    with pytest.raises(NameError):
        airport_dict = airport_lookup(parse_json(TEST_JSON), "Seattle-Tacoma International Airport")


def test_check_endpoint_airports():
    """Test to see if airport lookup function is working correctly."""
    from flight_paths import check_endpoint_airports, parse_json
    assert check_endpoint_airports(parse_json(TEST_JSON), "N'djili Airport", "Goma International Airport")


def test_check_endpoint_airports_not_in_data():
    """Test to see if airport lookup function is working correctly."""
    from flight_paths import check_endpoint_airports, parse_json
    with pytest.raises(NameError):
        check_endpoint_airports(parse_json(TEST_JSON), "Seattle-Tacoma International Airport", "Goma International Airport")


def test_find_path():
    """Test to see if airport lookup function is working correctly."""
    from flight_paths import find_path, parse_json
    assert ("N'djili Airport", 0) in find_path(parse_json(TEST_JSON), "Goma International Airport", "Test Airport")


def test_return_path():
    """Test to see if airport lookup function is working correctly."""
    from flight_paths import return_path, find_path, parse_json
    flight_path = find_path(parse_json(TEST_JSON), "Goma International Airport", "Test Airport")
    assert return_path(flight_path, parse_json(TEST_JSON))[0] == ["Test Airport", "N'djili Airport", "Goma International Airport"]

