# air quality api project

import mysql.connector
import requests
import json
import time

def connect_to_db():
    # TODO - connects to the 'cne340_finalproject' database
    con = mysql.connector.connect(
        user = 'root',
        password = '',
        host = '127.0.0.1',
        database = 'cne340_finalproject'
    )
    return con

def create_db_table(cursor):
    # TODO - creates a table in the 'cne340_finalproject' database
    pass

def query(cursor, query):
    # TODO - executes a query statement to a table in the 'cne340_finalproject' database
    cursor.execute(query)
    return cursor

def load_api_data():
    # TODO - sends a http request method (a get request) to the api
    api_key = '{INSERT API KEY HERE}'
    url = f'https://api.waqi.info/feed/Renton/?token={api_key}'
    response = requests.get(url)
    return json.loads(response.text)

def graph(dict):
    # TODO -
    #   graphs the air quality for the week and current month
    #   and saves an image of the graph in a folder (overrides previous saves)
    pass

def add_to_table(cursor, data):
    # TODO - adds a row into a table in the 'cne340_finalproject' database
    pass

def parse_forecast_data(dict, data):
    # TODO - parses data for date and average pm25 and adds them to dict
    forecast_data = data['data']['forecast']['daily']['pm25']
    for row in forecast_data:
        dict[row['day']] = row['avg']
    return dict

def check_if_day_exist():
    # TODO -
    #   returns true or false if the current day exist in the 'cne340_finalproject' database
    pass

def work():
    # TODO -
    #   parse api data (current and forecast) -
    #       create a dictionary and add the parsed data from current
    #       call parse_forecasts_data and reassign the value of the dictionary
    #   pass the dictionary into graph to create a graph
    #   add current data to the 'cne340_finalproject' database (only if the aqi for that day hasn't been added)
    pass

def main():
    con = connect_to_db()
    cursor = con.cursor()
    create_db_table(cursor)
    print('>> script: active')

    #while True:
        # TODO -
        #   work

        # 21600 seconds = 6 hours
        #time.sleep(21600)

if __name__ == '__main__':
    main()