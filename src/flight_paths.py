# -*- coding: utf-8 -*-

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


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, path)
            if newpath:
                return newpath
    return None

 # def find_path(graph, start, end, path=[]):
    # path = path + [start]
    # if start == end:
    #     return path
    # if not graph.has_key(start):
    #     return None
    # for node in graph[start]:
    #     if node not in path:
    #         newpath = find_path(graph, node, end, path)
    #         if newpath:
    #             return newpath
    # return None



data = parse_json(read_file(DATA_URL))
import pdb; pdb.set_trace()



# read_file
# parse_json
# find_path
# return_path_and_distance
