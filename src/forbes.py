# -*- coding: utf-8 -*-

"""
Returns the name, net worth, and industry of the **oldest
billionaire under 80 years old** AND the youngest billionaire with a valid age.
"""

import json
import os

JSON_FILE = "forbes_data.json"


def main():
    data = read_data()

    youngest_idx, oldest_idx = find_people(data)
    print(format_person('youngest', data[youngest_idx]))
    print(format_person('oldest', data[oldest_idx]))


def read_data(this_file=JSON_FILE):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, this_file)

    # Originally had this part of the program strip off the extra comma.
    f = open(abs_file_path, 'r')
    data = ''
    for line in f:
        data += line
    json_data = json.loads(data)

    return json_data


def find_people(data):
    """Will itterate through data to find the index of the oldest and youngest people."""
    youngest_idx = 0
    oldest_idx = 0

    for index, item in enumerate(data):
        if item['age'] < data[youngest_idx]['age'] and item['age'] > 0:
            youngest_idx = index
        if item['age'] > data[oldest_idx]['age'] and item['age'] < 80:
            oldest_idx = index
    return youngest_idx, oldest_idx


def format_person(adj, dict):
    """Format the output of the script."""
    name = dict['name']
    net = int(dict['net_worth (USD)'])
    return "The {0} person is {1}.  They have a net worth of ${2:,}".format(adj, name, net)

main()
