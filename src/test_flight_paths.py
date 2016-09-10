# -*- coding: utf-8 -*-
import pytest

from flight_paths import DATA_URL

TEST_JSON = '''[{"city": "Goma", "connection_urls": ["https://en.wikipedia.org/wiki/Kindu_Airport", "https://en.wikipedia.org/wiki/Bangoka_International_Airport", "https://en.wikipedia.org/wiki/N%27djili_Airport", "https://en.wikipedia.org/wiki/Addis_Ababa_Bole_International_Airport"], "url": "https://en.wikipedia.org/wiki/Goma_International_Airport", "country": "Democratic Republic of the Congo", "destination_cities": ["Kinshasa", "Kisangani", "Addis Ababa"], "destination_airports": ["N'djili Airport", "Bangoka International Airport", "Addis Ababa Bole International Airport"], "airport": "Goma International Airport", "lat_lon": [-1.669889, 29.238278]}, {"city": "Kinshasa", "connection_urls": ["https://en.wikipedia.org/wiki/Port_Bouet_Airport", "https://en.wikipedia.org/wiki/Libreville_International_Airport", "https://en.wikipedia.org/wiki/Paris-Charles_de_Gaulle", "https://en.wikipedia.org/wiki/Gemena_Airport", "https://en.wikipedia.org/wiki/Kananga_Airport", "https://en.wikipedia.org/wiki/Mbandaka_Airport", "https://en.wikipedia.org/wiki/Mbuji_Mayi_Airport", "https://en.wikipedia.org/wiki/Douala_International_Airport", "https://en.wikipedia.org/wiki/Murtala_Muhammed_International_Airport", "https://en.wikipedia.org/wiki/Maya-Maya_Airport", "https://en.wikipedia.org/wiki/Libreville_International_Airport", "https://en.wikipedia.org/wiki/Lom%C3%A9%E2%80%93Tokoin_Airport", "https://en.wikipedia.org/wiki/Brussels_Airport", "https://en.wikipedia.org/wiki/Maya-Maya_Airport", "https://en.wikipedia.org/wiki/Douala_International_Airport", "https://en.wikipedia.org/wiki/Goma_International_Airport", "https://en.wikipedia.org/wiki/Kananga_Airport", "https://en.wikipedia.org/wiki/Kindu_Airport", "https://en.wikipedia.org/wiki/Bangoka_International_Airport", "https://en.wikipedia.org/wiki/Lubumbashi_International_Airport", "https://en.wikipedia.org/wiki/Mbandaka_Airport", "https://en.wikipedia.org/wiki/Mbuji_Mayi_Airport", "https://en.wikipedia.org/wiki/Bole_International_Airport", "https://en.wikipedia.org/wiki/Jomo_Kenyatta_International_Airport", "https://en.wikipedia.org/wiki/Mohammed_V_International_Airport", "https://en.wikipedia.org/wiki/OR_Tambo_International_Airport", "https://en.wikipedia.org/wiki/Quatro_de_Fevereiro_Airport", "https://en.wikipedia.org/wiki/Istanbul-Atat%C3%BCrk", "https://en.wikipedia.org/wiki/Libreville_International_Airport"], "url": "https://en.wikipedia.org/wiki/N%27djili_Airport", "country": "Democratic Republic of the Congo", "destination_cities": ["Goma", "Kisangani", "Lubumbashi", "Brazzaville", "Nairobi", "Casablanca", "Luanda", "Kempton Park", "Abidjan"], "destination_airports": ["Goma International Airport", "Bangoka International Airport", "Lubumbashi International Airport", "Maya-Maya Airport", "Jomo Kenyatta International Airport", "Mohammed V International Airport", "Quatro de Fevereiro Airport", "OR Tambo International Airport", "Port Bouet Airport"], "airport": "N'djili Airport", "lat_lon": [-4.38575, 15.4445694]}]'''


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
