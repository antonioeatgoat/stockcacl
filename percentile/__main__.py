from percentile.api import alpha as api_interface
from percentile.exception.InvalidApiKeyException import InvalidApiKeyException
from percentile.exception.InvalidApiCallException import InvalidApiCallException
from percentile.exception.ApiGenericException import ApiGenericException
from percentile.exception.TooManyRequestsException import TooManyRequestsException
import percentile._interface.input as percentile_input
import percentile._interface.output as percentile_output
import percentile.percentile
from dotenv import load_dotenv
import os
import sys

load_dotenv()

symbol = percentile_input.fetch_symbol()

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

prices = percentile.extract_prices(response)

earnings = percentile.calculate_earnings(prices[:36 * 5 + 1])

weekly_earnings = percentile.group_by_weeks(earnings, 36)

percentile = percentile.calculate_percentile(weekly_earnings)

if percentile_input.is_numeric_output():
    percentile_output.print_numeric_percentile(percentile)
else:
    percentile_output.print_weeks_earnings(response, weekly_earnings)
    percentile_output.print_percentile(percentile)