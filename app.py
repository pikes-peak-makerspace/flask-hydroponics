# Get the things we need to run our Flask webserver
from flask import Flask, render_template, redirect, url_for, session, jsonify

# Imported for reading Pi sensors
import os
import glob
import time
import re
import json

# Only used for initial route testing
import random

# Initialize modprobe stuff to read one-wire devices
# like a water proof temp sensor: DS18B20
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# path of the all the temp sensors
base_dir = '/sys/bus/w1/devices/'

# file location in each sensor
file_location = '/w1_slave'

# full list of all the temp sensors unique ID
# temp_sensors = ['28-00000729be6e', '28-000007291af0', '28-000007296c0d', '28-0000072a26c3', '28-0000072a2e50']
temp_sensors = ['28-000007296c0d']

# Loops through each sensor and prepends and
# appends the dir and file location to each.
temp_sensor_paths = []
for sensor in temp_sensors:
    temp_sensor_paths.append(base_dir + sensor + file_location)
    
# make regex to find 'YES'
yesRegex = re.compile(r'''(
    (YES)
)''', re.VERBOSE)

# make regex to find temp reading
tempRegex = re.compile(r'''(
    (t=\d+)
)''', re.VERBOSE)

# Create flask instance
app = Flask(__name__)

# Main route
@app.route("/")
def index():
    # Read in some JSON
    with open('db/ds18b20.json') as json_file:
        data = json.load(json_file)
        # sensors = []
        # for sensor in data['ds18b20-sensors']:
        #     sensor_id = sensor['id']
        #     serial = sensor['serial']
        #     sensors.append(sensor['serial'])
        #     physical_location = sensor['physical-location']

        # print(sensors)
        # Prints all the json in the db file
        # print(data['ds18b20-sensors'])
        # Grabs the serial data in the first object of the json
        # print(data['ds18b20-sensors'][0]['serial'])

    data_type = type(data)
    return render_template("index.html", title="Home", data=data, data_type=data_type)

# Temperature route
@app.route('/temp')
def temp():
    # read temp from sensor file
    def read_temp_raw():
        f = open(temp_sensor_paths[0], 'r')
        lines = str(f.readlines())
        f.close()
        return lines

    # make raw data pretty
    def read_temp():
        lines = read_temp_raw()
        for groups in yesRegex.findall(lines):
            if groups[0] != 'YES':
                time.sleep(0.5)
                lines = read_temp_raw()
            for groups in tempRegex.findall(lines):
                temp = groups[0]
                temp_number = temp[2:]
                if temp_number != -1:
                    return temp_number
                else:
                    return 'Temp error: value = -1'

    # calculate to celcius and farenheit
    def calc_temps():
        temp = read_temp()
        temp_c = float(temp) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

    # Save to file function.
    # Not currently being used.
    def save_to_file():
        get_temps = calc_temps()
        temp_c = str(get_temps[0])
        temp_f = str(get_temps[1])
        data_file = open('temp_data.txt', 'a')
        data_file.write('Celcius: ' + temp_c + ' Fahrenheit: ' + temp_f)
        data_file.close()
        
    def get_temp_data():
        get_temps = calc_temps()
        temp_c = str(get_temps[0])
        temp_f = str(get_temps[1])
        return temp_f
        
    # Call to get the temp values
    temp_f = get_temp_data()
    
    # Render the template for this route with data
    return render_template('temp.html', temp_f=temp_f)

@app.route('/json-response')
def json_response():
    # read temp from sensor file
    def read_temp_raw():
        f = open(temp_sensor_paths[0], 'r')
        lines = str(f.readlines())
        f.close()
        return lines

    # make raw data pretty
    def read_temp():
        lines = read_temp_raw()
        for groups in yesRegex.findall(lines):
            if groups[0] != 'YES':
                time.sleep(0.5)
                lines = read_temp_raw()
            for groups in tempRegex.findall(lines):
                temp = groups[0]
                temp_number = temp[2:]
                if temp_number != -1:
                    return temp_number
                else:
                    return 'Temp error: value = -1'

    # calculate to celcius and farenheit
    def calc_temps():
        temp = read_temp()
        temp_c = float(temp) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
        
    def get_temp_data():
        get_temps = calc_temps()
        temp_c = str(get_temps[0])
        temp_f = str(get_temps[1])
        return temp_f
        
    # Call to get the temp values
    temp_f = get_temp_data()
    
    return jsonify(temp_f=temp_f)