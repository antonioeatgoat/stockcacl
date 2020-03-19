from stockcalc.exception.PercentileException import PercentileException


class TooManyRequestsException(PercentileException):
    """Exception raised if the API calls quota is exceeded

    Attributes:
        response -- message from API
    """

    def __init__(self, response):
        self.response = response

    def __str__(self):
        return self.response
