TEST_JSON = [
    {
        "name": "Bill Gates",
        "age": 60,
        "rank": 1,
        "net_worth (USD)": 75000000000,
        "source": "Microsoft",
        "country": "United States"
    },
    {
        "name": "Warren Buffett",
        "age": 85,
        "rank": 3,
        "net_worth (USD)": 60800000000,
        "source": "Berkshire Hathaway",
        "country": "United States"
    },
    {
        "name": "Carlos Slim Helu",
        "age": 76,
        "rank": 1,
        "net_worth (USD)": 50000000000,
        "source": "telecom",
        "country": "Mexico"
    },
    {
        "name": "Jeff Bezos",
        "age": 52,
        "rank": 5,
        "net_worth (USD)": 45200000000,
        "source": "Amazon.com",
        "country": "United States"
    }
]


def test_read_data():
    """Test to see if expected data is in file read."""
    from forbes import read_data
    data = read_data()
    assert 'Bill Gates' in data[0]['name']


def test_read_data_end_of_file():
    """
    Test to see if expected data is in file read.
    Something near the end to check if all data being read.
    """
    from forbes import read_data
    data = read_data()
    assert 'Paul Allen' in data[-1]['name']


def test_find_people_youngest():
    """Test to see if the algorith finds youngest person."""
    from forbes import find_people
    index = find_people(TEST_JSON)[0]
    assert index == 3


def test_find_people_oldest():
    """Test to see if the algorith finds youngest person."""
    from forbes import find_people
    index = find_people(TEST_JSON)[1]
    assert index == 2


def test_format_person_name():
    """Test the format function to see if has name."""
    from forbes import format_person
    my_dict = TEST_JSON[0]
    assert 'Bill Gates' in format_person('funniest', my_dict)


def test_format_person_net_worth():
    """Test the format function to see if has name."""
    from forbes import format_person
    my_dict = TEST_JSON[0]
    assert '$75,000,000,000' in format_person('funniest', my_dict)

