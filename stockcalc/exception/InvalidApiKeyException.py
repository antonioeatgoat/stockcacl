from stockcalc.exception.PercentileException import PercentileException


class InvalidApiKeyException(PercentileException):
    """Exception raised for errors related to API key.

    Attributes:
        response -- message from API
    """

    def __init__(self, response):
        self.response = response

    def __str__(self):
        return self.response
