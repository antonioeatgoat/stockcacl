from api import alphavantage as api_interface
import core
from dotenv import load_dotenv
import interface.input
import interface.output
import os

load_dotenv()

symbol = interface.input.fetch_symbol()

response = api_interface.fetch(symbol, os.getenv("APIKEY"))

prices = core.extract_prices(response)

earnings = core.calculate_earnings(prices[:36*5+1])

weekly_earnings = core.group_by_weeks(earnings, 36)

percentile = core.calculate_percentile(weekly_earnings)

interface.output.print_weeks_earnings(response, weekly_earnings)
interface.output.print_percentile(percentile)
