def print_weeks_earnings(day_series: dict, earnings: [float]):
    print('\n')
    print('List of the weekly average earnings:')

    # todo move this logic outside
    days = list(day_series.keys())
    for i, earn in enumerate(earnings):
        print(f'{days[i*5]}: {round(earn*100)}%')


def print_percentile(percentile: float):
    print('\n')
    print(f'The percentile value is {percentile*100}')


def print_numeric_percentile(percentile: float):
    print(percentile * 100)
