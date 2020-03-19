import pandas
import numpy


def extract_prices(days_series: dict) -> []:
    """Given a dictionary of days => prices, returns an array containing the list of the prices"""

    return list(days_series.values())


def group_by_weeks(prices: [], weeks_limit: int) -> []:
    """Given a dictionary of days, group them by five and return a array containing the mean of each group"""

    days_limit = weeks_limit * 5
    n_prices = len(prices)
    weekly_averages = []

    for i in range(0, n_prices, 5):
        end_range = i+5

        if end_range >= n_prices or end_range > days_limit:
            break

        weekly_averages.append(numpy.mean(prices[i:end_range]))

    return weekly_averages


def calculate_earnings(prices: []) -> []:
    """Given an array of prices, iterate it calculating the earnings of each prices based on the previous one"""

    p = pandas.Series(reversed(prices))

    prices = list(reversed(p.pct_change().round(2)))

    return prices[:-1]


def calculate_percentile(prices: []):
    percentiles = pandas.DataFrame(prices).rank(pct=True)

    return percentiles[0].round(2).tolist()[0]

