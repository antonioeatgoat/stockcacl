from stockcalc.exception.PercentileException import PercentileException


class InvalidApiCallException(PercentileException):
    """Exception raised for an invalid API call

    Attributes:
        response -- message from API
    """

    def __init__(self, response):
        self.response = response

    def __str__(self):
        return self.response
