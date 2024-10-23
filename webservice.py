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
def getStockData(symbol, time_series_function):
    url = f"https://www.alphavantage.co/query?function={time_series_function}&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if 'Error Message' in data:
        print(f"Error: No data available for the stock symbol '{symbol}'")
        return None
    elif not data:
        print("Error: No data returned by the API.")
        return None
    
    return data

# Function to validate date
def validateDate(prompt):
    while True:
        user_input = input(prompt)
        try:
            return datetime.striptime(user_input, '%Y-%m-%d')
        except:
            print('Invalid date format. Please enter in YYYY-MM-DD format.')

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
    while True:
    
        chart_type = 0
        timeSeriesFunction = 0
    
    
        print("Stock Data Visualizer\n---------------------------")


        # Ask user to select chart type
    
        chart_type = getChartType()

        # Ask user to select time series function

        timeSeriesFunction = getTimeSeriesFunction()


        # Ask user for date range

        begin_date = validateDate("Enter the beginning date (YYY-MM-DD):")
        end_date = validateDate("Enter the end date (YYYY-MM-DD):")


        # Ensure end date is not before the begin date
        if end_date < begin_date:
            print("End date cannot be earlier than the start date. Please try again.")
            continue


        # Fetch stock data from Alpha Vantage


        # Convert dates to strings for comparison


        # Plot chart based on user's choice


        # Ask if user wants to continue


if __name__ == "__main__":
    main()