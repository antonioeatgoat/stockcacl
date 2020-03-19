# Stock Calculator - Percentile Analysis

A simple python module to perform percentile analysis on stock data

## Installation

Linux user can install it using pip:

    sudo pip install --upgrade stockcalc

This command will update youtube-dl if you have already installed it.

## Description

StockCalc is a simple command line program that allows you to perform percentile analysis on stock data.
You can choose the stock equity to analyse and it will provide the percentile position of the average earnings of 
the last week, on the line represented by the latest six months.

The percentile value is expressed as an integer.

    python3 -m stockcalc ANX.LON [OPTIONS] 

If you don't specify a stock symbol, it will be the first thing asked by the program before go ahead.

## Options

    --numeric               It returns just the numeric percentile (float) instead of a more verbose result,
                            which also contains the average earnings of the latest twentfour weeks.
                            
## Coming Soon
- An option to specify a different apikey without edit the .env file.
- An option to specify how many weeks you want to use for the percentile analysis.
- An option to see the current version of the installed package.

## Credits
- [Alpha Vantage](https://www.alphavantage.co/): it provides the APIs called by this package to fetch the stock data.