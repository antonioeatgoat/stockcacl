import unittest
import percentile.percentile


class TestsPercentile(unittest.TestCase):
    closing_prices = {
        '2020-03-10': 5,
        '2020-03-9': 3,
        '2020-03-8': 6,
        '2020-03-7': 8,
        '2020-03-6': 10,
        '2020-03-5': 3,
        '2020-03-4': 2,
        '2020-03-3': 8,
        '2020-03-2': 8,
        '2020-03-1': 5,
        '2020-02-29': 3,
        '2020-02-28': 4,
        '2020-02-27': 6,
        '2020-02-26': 7,
        '2020-02-25': 6,
        '2020-02-24': 6,
    }

    def test_calculates_weekly_average_prices(self):
        expected = [6.4, 5.2, 5.2]

        prices = percentile.extract_prices(self.closing_prices)

        # Limit minor than number of days
        self.assertEqual(expected, percentile.group_by_weeks(prices, 3))

        # Limit partially exceeding the number of days
        self.assertEqual(expected, percentile.group_by_weeks(prices, 4))

        # Limit exceeding the number of days by more than one week
        self.assertEqual(expected, percentile.group_by_weeks(prices, 5))

    def test_calculate_earnings(self):
        expected = [.67, -.5, -.25, -.20, 2.33, .50, -.75, 0.0, .60, .67, -.25, -.33, -.14, .17, 0.0]

        prices = percentile.extract_prices(self.closing_prices)

        self.assertEqual(expected, percentile.calculate_earnings(prices))

    def test_calculate_percentile(self):
        expected = 0.9

        prices = percentile.extract_prices(self.closing_prices)

        earnings = percentile.calculate_earnings(prices)

        self.assertEqual(expected, percentile.calculate_percentile(earnings))


if __name__ == '__main__':
    unittest.main()