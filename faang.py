# This program uses the yfinance package to download and visualize hourly stock data
# for the five FAANG companies: META, AAPL, AMZN, NFLX, and GOOG.
# And the function called 'plot_data()' loads the most recent CSV file from the 'data/' directory,
# to create a plot of the closing prices for all 5 stocks, and saves the plot.
# Author: Tanya San Juan

#! /usr/bin/env python


# Dates and times
import datetime as dt 

# Yahoo Finance data
import yfinance as yf

# Create a Function 'get_data()'

def get_data():
    df = yf.download(
        ["META", "AAPL", "AMZN", "NFLX", "GOOG"],
        period="5d",
        interval="1h")

    # To get the current date and time
    now = dt.datetime.now()
    # Format date and time.
    now.strftime("%Y%m%d-%H%M%S")

    #File name.
    filename = "./data/" + now.strftime("%Y%m%d-%H%M%S") + ".csv"

# Save CSV
    df.to_csv("./data/" + dt.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv")
