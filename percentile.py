from api import alphavantage as api_interface
from dotenv import load_dotenv
import os

load_dotenv()

print(api_interface.fetch('EXSA.DE', os.getenv("APIKEY")))
