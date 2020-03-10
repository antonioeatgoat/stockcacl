"""
Api interface to fetch prices data from Alpha Vantage api

Documentation: https://www.alphavantage.co/documentation/
Get apikey: https://www.alphavantage.co/support/#api-key
"""

import requests


def fetch(symbol: str, apikey: str) -> dict:
    """Returns a dictionary containing the list of daily closing prices, indexed by date"""
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={apikey}'
    return _parse_alpha_response(_make_request(url))


def _make_request(url: str) -> requests.Response:
    """Executes the actual api request"""
    return requests.get(url)


def _parse_alpha_response(response: requests.Response) -> dict:
    """Converts the data coming from api to an expected format"""
    data = response.json()
    parsed_data = {}

    for day, values in list(data.values())[1].items():
        parsed_data[day] = list(values.values())[3]

    return parsed_data
