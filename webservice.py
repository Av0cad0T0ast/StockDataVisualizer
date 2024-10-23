import requests
import pygal
from datetime import datetime

API_KEY = '5JUJV1WUJIBMM95'

# Function to get chart type

def getChartType():
    user_input = 0
    while(True):
        print("Chart Types\n---------------------")
        print("1. Bar")
        print("2. Line")
        user_input = input("Enter the chart type you want (1, 2): ")
        if(int(user_input) == 1 or int(user_input) == 2):
            break
    return user_input

# Function to get time series function
def getTimeSeriesFunction():
    while(True):
        print("\nTime Series Options\n-----------------")
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly")
        user_input = input("Enter the time series you want (1-4): ")
        if user_input in ['1', '2', '3', '4']:
            time_series_map = {
                '1': 'TIME_SERIES_INTRDAY&interval=60min',
                '2': 'TIME_SERIES_DAILY',
                '3': 'TIME_SERIES_WEEKLY',
                '4': 'TIME_SERIES_MONTHLY'
            }
            return time_series_map[user_input]


# Function to get stock data
def getStockData(symbol, time_series_function):
    url = f"https://alphavantage.co/query?function={time_series_function}&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

# Function to validate date


# Function to plot chart


    # Create chart type


    # Extract data


    # Set chart title and values


    # Render chart to an svg and open in browser


# Main Loop

def main():
    chart_type = 0

    # Ask user to select chart type
    
    chart_type = getChartType()


    # Ask user to enter stock symbol
    symbol = input("Enter the stock symbol (e.g., GOOGL for Google): ")

    # Ask user to select time series function
    time_series_function = getTimeSeriesFunction()

    # Map users choice to API function names


    # Fetch stock data from Alpha Vantage


    # Filter data based on the date range


    # Plot chart based on user's choice


    # Ask if user wants to continue


if __name__ == "__main__":
    main()