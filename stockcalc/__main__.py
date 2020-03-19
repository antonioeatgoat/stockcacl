from stockcalc.api import alpha as api_interface
from stockcalc.exception.InvalidApiKeyException import InvalidApiKeyException
from stockcalc.exception.InvalidApiCallException import InvalidApiCallException
from stockcalc.exception.ApiGenericException import ApiGenericException
from stockcalc.exception.TooManyRequestsException import TooManyRequestsException
import stockcalc._interface.input as percentile_input
import stockcalc._interface.output as percentile_output
import stockcalc.core
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
    print("It seems there is a problem with your API call. Probably you are using a wrong symbol.")
    sys.exit(1)
except (ApiGenericException, TooManyRequestsException) as err:
    print(err)
    sys.exit(1)

prices = stockcalc.core.extract_prices(response)

earnings = stockcalc.core.calculate_earnings(prices[:36 * 5 + 1])

weekly_earnings = stockcalc.core.group_by_weeks(earnings, 36)

percentile = stockcalc.core.calculate_percentile(weekly_earnings)

if percentile_input.is_numeric_output():
    percentile_output.print_numeric_percentile(percentile)
else:
    percentile_output.print_weeks_earnings(response, weekly_earnings)
    percentile_output.print_percentile(percentile)
