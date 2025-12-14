'''This program uses the yfinance package to download and visualize hourly stock data
for the five FAANG companies: META, AAPL, AMZN, NFLX, and GOOG.
And the function called 'plot_data()' loads the most recent CSV file from the 'data/' directory,
to create a plot of the closing prices for all 5 stocks, and saves the plot.
'''
# Author: Tanya San Juan

#! /usr/bin/env python

# Dates and times
import datetime as dt 

# Yahoo Finance data
import yfinance as yf

# Operating system
import os

# import DataFrames
import pandas as pd

# import matplotlib for plotting
import matplotlib.pyplot as plt


# Create a Function 'get_data()'
def get_data():
    '''Download the FAANG hourly for the last 5 days and save it in a folder called (data)'''
    tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]

    # Download hourly prices for the past 5 days
    df = yf.download(tickers, period="5d", interval="1h")
    
    
    # Save data as CSV
    # Source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True) #This create a directory if doesn't exist

    '''Format to the data and time. We can use 'now.strftime'''
    # File name with format date and time.
    filename = dt.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
    filename_time = f"{data_dir}/{filename}"

    '''The return keyword is to exit a function and return a value. Source: https://www.w3schools.com/python/ref_keyword_return.asp'''
    df.to_csv(filename_time)
    return df, filename_time

# call the function
data, file_path = get_data()
print(f"Data saved to {file_path}")
# print the first 5 rows of the data
print(data.head())