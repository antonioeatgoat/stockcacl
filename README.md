# Stock Calculator - Percentile Analysis

A simple python module to perform percentile analysis on stock data

## Installation

Linux user can install it using pip:

    sudo -H pip install --upgrade stockcalc

This command will update youtube-dl if you have already installed it.

## Description

StockCalc is a simple command line program that allows you to perform percentile analysis on stock data.
You can choose the stock equity to analyse and it will provide the percentile position of the average earnings of 
the last week, on the line represented by the latest six months.

The percentile value is expressed as an integer.

    python3 -m stockcalc ANX.LON [OPTIONS] 

## Options

    --numeric               It returns just the numeric percentile (float) instead of a more verbose result,
                            which also contains the average earnings of the latest twentfour weeks.