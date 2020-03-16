from api import alpha as api_interface
from exception.InvalidApiKeyException import InvalidApiKeyException
from exception.InvalidApiCallException import InvalidApiCallException
from exception.ApiGenericException import ApiGenericException
from exception.TooManyRequestsException import TooManyRequestsException
import core
from dotenv import load_dotenv
import interface.input
import interface.output
import os
import sys

load_dotenv()

symbol = interface.input.fetch_symbol()

try:
    response = api_interface.fetch(symbol, os.getenv("APIKEY"))
except InvalidApiKeyException as err:
    print("It seems there is a problem with your API key. Did you fill your .env file?")
    print(err)
    sys.exit(1)
except InvalidApiCallException as err:
    print("It seems there is a problem with your API key. Probably you are using a wrong symbol.")
    sys.exit(1)
except (ApiGenericException, TooManyRequestsException) as err:
    print(err)
    sys.exit(1)


prices = core.extract_prices(response)

earnings = core.calculate_earnings(prices[:36*5+1])

weekly_earnings = core.group_by_weeks(earnings, 36)

percentile = core.calculate_percentile(weekly_earnings)

if interface.input.is_numeric_output():
    interface.output.print_numeric_percentile(percentile)
else:
    interface.output.print_weeks_earnings(response, weekly_earnings)
    interface.output.print_percentile(percentile)
