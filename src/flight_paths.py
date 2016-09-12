# -*- coding: utf-8 -*-
"""Return a flight path between two airports."""
from future.standard_library import install_aliases
install_aliases()

from urllib.request import urlopen
import json


DATA_URL = 'https://codefellows.github.io/sea-python-401d4/_downloads/cities_with_airports.json'


def read_file(url):
    """Read a file from the internets."""
    response = urlopen(url)
    html = response.read()
    return html.decode('utf-8')


def parse_json(data):
    """Parse a json request."""
    json_data = json.loads(data)
    return json_data


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3 # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])

    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934 # convert km to miles


def airport_lookup(json_data, airport):
    """look-up an airport and return the dictionary with that entry."""
    try:
        return next((item for item in json_data if item["airport"] == airport))
    except StopIteration:
        raise NameError("{} not found in list of airports.".format(airport))


def check_endpoint_airports(json_data, start, end):
    """Return a NameError if either airport is not in data."""
    airport_lookup(json_data, start)
    airport_lookup(json_data, end)
    return True


def find_path(json_data, start_airport, end_airport):
    """Does a breadth transversal until it finds the end airport."""
    airport_list = [(start_airport, None)]
    current_airport = start_airport
    index = 0
    is_done = False
    while not is_done:
        current_airport_dict = airport_lookup(json_data, current_airport)
        for destination in current_airport_dict['destination_airports']:
            airport_list.append((destination, index))
            if destination == end_airport:
                is_done = True
                break
        index += 1
        current_airport = airport_list[index][0]
    return airport_list


def return_path(airport_list, json_data):
    """Take list from find_path and return a list for a flight path."""
    current_index = -1
    start_airport = airport_list[current_index][0]
    my_list = [start_airport]
    start_airport_dict = airport_lookup(json_data, start_airport)
    start_lat_lon = start_airport_dict['lat_lon']
    milage = 0
    while current_index:
        current_index = airport_list[current_index][1]
        end_airport = airport_list[current_index][0]
        end_airport_dict = airport_lookup(json_data, end_airport)
        end_lat_lon = end_airport_dict['lat_lon']
        milage += calculate_distance(start_lat_lon, end_lat_lon)
        my_list.append((airport_list[current_index][0]))
        start_lat_lon = end_lat_lon

    return my_list, milage


def main(start, end):
    """Take a start and end airports and return a path and milage."""
    data = parse_json(read_file(DATA_URL))
    check_endpoint_airports(data, start, end) 
    search_path = find_path(data, start, end)
    path = return_path(search_path, data)
    print(path)


if __name__ == '__main__':
    main()
