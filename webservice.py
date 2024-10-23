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

# Function to get stock data


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


    # Ask user to select time series function


    # Map users choice to API function names


    # Fetch stock data from Alpha Vantage


    # Filter data based on the date range


    # Plot chart based on user's choice


    # Ask if user wants to continue


if __name__ == "__main__":
    main()