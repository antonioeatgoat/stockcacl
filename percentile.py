from api import alphavantage as api_interface
from dotenv import load_dotenv
import os
import sys

load_dotenv()


if 1 < len(sys.argv):
    symbol = sys.argv[1]
else:
    symbol = input('Please provide a symbol to analyse:\n')


print(api_interface.fetch(symbol, os.getenv("APIKEY")))
