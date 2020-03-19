from stockcalc.exception.PercentileException import PercentileException


class ApiGenericException(PercentileException):
    """Exception raised for an unidentified API error

    Attributes:
        response -- message from API
    """

    def __init__(self, response):
        self.response = response

    def __str__(self):
        return self.response
