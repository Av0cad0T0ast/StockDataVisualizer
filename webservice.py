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

# Function to get Time series
def getTimeSeriesFunction():
    user_input = 0
    while(True):
        print("Select the Time Series of the chart you want to generate")
        print("--------------------------------------------------------")
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly")
        user_input = input("Enter time series function (1, 2, 3, 4): ")
        if(int(user_input) < 0 or int(user_input) < 5):
            break
    return user_input

# Function to get stock data


# Function to validate date


# Function to plot chart
def plot_chart(chart_type, data, title):

    # Create chart type
    if chart_type == 1:
        chart = pygal.Bar()
    elif chart_type == 2:
        chart = pygal.Line()
    else:
        print("Invalid chart type")
        return
    
    # Extract data and set chart values
    dates = []
    values = []
    for date, daily_data in sorted(data.items()):
        dates.append(date)
        values.append(float(daily_data['4. close']))

    chart.title = title
    chart.x_labels = dates
    chart.add('Price', values)

    # Render chart to an svg and open in browser
    chart.render_in_browser()


# Main Loop

def main():
    chart_type = 0
    timeSeriesFunction = 0
    
    
    print("Stock Data Visualizer\n---------------------------")


    # Ask user to select chart type
    
    chart_type = getChartType()

    # Ask user to select time series function

    timeSeriesFunction = getTimeSeriesFunction()

    # Map users choice to API function names


    # Fetch stock data from Alpha Vantage


    # Filter data based on the date range


    # Plot chart based on user's choice


    # Ask if user wants to continue


if __name__ == "__main__":
    main()