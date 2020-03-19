"""
Api _interface to fetch prices data from Alpha Vantage api

Documentation: https://www.alphavantage.co/documentation/
Get apikey: https://www.alphavantage.co/support/#api-key
"""

import requests
from stockcalc.exception.InvalidApiKeyException import InvalidApiKeyException
from stockcalc.exception.InvalidApiCallException import InvalidApiCallException
from stockcalc.exception.ApiGenericException import ApiGenericException
from stockcalc.exception.TooManyRequestsException import TooManyRequestsException


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

    __validate_data(data)

    parsed_data = {}
    for day, values in list(data.values())[1].items():
        parsed_data[day] = float(list(values.values())[3])

    return parsed_data


def __validate_data(data: {}):
    """Validate the data returned by API"""
    if "Error Message" in data:
        if "apikey is invalid" in data["Error Message"]:
            raise InvalidApiKeyException(data["Error Message"])
        elif "Invalid API call" in data["Error Message"]:
            raise InvalidApiCallException(data["Error Message"])
        else:
            raise ApiGenericException(data["Error Message"])
    elif "Note" in data and "API call frequency" in data['Note']:
        raise TooManyRequestsException(data['Note'])
