# Get the things we need to run our Flask webserver and other utilities.
from flask import Flask, render_template, redirect, url_for, session, jsonify

# Imported for reading Pi sensors and various other things.
import os
import glob
import time
import re
import json
import sys

# Check if the device is a Raspberry Pi or not
# TODO This only checks if the OS is rasbian. Need to check more things to make sure its a pi.
try:
    # Path of the file we are checking for info
    pi_check_path = "/etc/os-release"
    # Open the file and save to variable
    with open(pi_check_path, 'r') as pi_check_file:
        # Read the file and save it into the same var name
        pi_check_file = pi_check_file.read()
    # Look for a specific line in the file
    if "ID=raspbian" in pi_check_file:
        print("Raspberry Pi detected! Setting is_raspberry_pi to True")
        is_raspberry_pi = True
    # Check if there is a line and if so if it is equal to raspbian
# If it's not a pi then set pi setting to false
except:
    print("Raspberry Pi NOT detected! Setting is_raspberry_pi to False")
    print("Some features will be disabled or replaced with dummy data.")
    is_raspberry_pi = False

# Initialize modprobe to read one-wire devices.
# Like a water proof temp sensor: DS18B20
if is_raspberry_pi:
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

# Change the symbols Jinja uses to let view take rendering control
class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',  # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_end_string='%%',
    ))

# Create flask app. Note the updated class name.
app = CustomFlask(__name__)

# Main route of app. This serves a Vuejs application.
@app.route("/")
def index():
    # This route returns the index.html template.
    return render_template("index.html")

# Path to the 1 wire devices
one_wire_devices_path = "/sys/bus/w1/devices/"

# Route to get data of available temp sensors
@app.route("/1wire-devices")
def get_1wire_devices():
    # Get available w1 devices if on the raspberry pi
    if not is_raspberry_pi:
        # Respond with message about device not being a raspberry pi
        dir_output = "Not on a Raspberry Pi!"
    else: 
        # TODO check if there are no devices and respond accordingly
        # Get a list of the devices
        dir_output = os.listdir(one_wire_devices_path)
        # Remove the master device from the list
        dir_output.remove('w1_bus_master1')       
    return jsonify(dir_output)




# The following is setup for reading and parsing the
# ds18b20 tempertaure sensor data + routes to get temp data.
# File system path of the all the temp sensors.
base_dir = '/sys/bus/w1/devices/'

# File location in each sensor folder.
# This is where the live temp data is sent
# and captured from. It is parsed with a REGEX.
file_location = '/w1_slave'

# Full list of all the temp sensors unique IDs. 
# These were manaully checked in the file system
# when plugged in and then added here.
temp_sensors = ['28-00000729be6e', '28-000007291af0',
                '28-000007296c0d', '28-0000072a26c3',
                '28-0000072a2e50']

# Loops through each sensor and prepends and
# appends the dir and file location to each.
temp_sensor_paths = []
for sensor in temp_sensors:
    # Each sensor will have a path constructed like:
    # /sys/bus/w1/devices/28-00000729be6e/w1_slave
    temp_sensor_paths.append(base_dir + sensor + file_location)
    
# Make regex to find 'YES'.
# This ensures the sensor is working and reading data.
yesRegex = re.compile(r'''(
    (YES)
)''', re.VERBOSE)

# Make regex to find temp reading.
# This gets value after the 't=' characters.
tempRegex = re.compile(r'''(
    (t=\d+)
)''', re.VERBOSE)

# Temperature sensor routes (ds18b20). Multiple routes.

# URL of the route. Returns JSON with temp reading
# and the location of the sensor in the physical 
# enviroment.
@app.route('/sensor/ds18b20/sensor_0')
def ds18b20_sensor_0():
        
    serial_number = '28-00000729be6e'
    # Call to get the temp values.
    # Pass the index of the correct temp sensor.
    # Returns the temps in F and C.
    try:
        temps = get_temp_data(temp_sensor_paths[0])
    except: 
        temps = 'No sensor connected :('
    
    # Manully set location of the sensor, for now.
    location = 'unknown'
    
    # Render the template for this route with data.
    # Read and display the JSON with JS calls on the index page.
    return jsonify(serial_number=serial_number, temps=temps, location=location)

# URL of the route. Returns JSON with temp reading
# and the location of the sensor in the physical 
# enviroment.
@app.route('/sensor/ds18b20/sensor_1')
def ds18b20_sensor_1():
        
    serial_number = '28-000007291af0'
    # Call to get the temp values.
    # Pass the index of the correct temp sensor.
    # Returns the temps in F and C.
    try:
        temps = get_temp_data(temp_sensor_paths[1])
    except: 
        temps = 'No sensor connected :('
    
    # Manully set location of the sensor, for now.
    location = 'unknown'
    
    # Render the template for this route with data.
    # Read and display the JSON with JS calls on the index page.
    return jsonify(serial_number=serial_number, temps=temps, location=location)

# URL of the route. Returns JSON with temp reading
# and the location of the sensor in the physical 
# enviroment.
@app.route('/sensor/ds18b20/sensor_2')
def ds18b20_sensor_2():
        
    serial_number = '28-000007296c0d'
    # Call to get the temp values.
    # Pass the index of the correct temp sensor.
    # Returns the temps in F and C.
    try:
        temps = get_temp_data(temp_sensor_paths[2])
    except: 
        temps = 'No sensor connected :('   
    # Manully set location of the sensor, for now.
    location = 'unknown'
    
    # Render the template for this route with data.
    # Read and display the JSON with JS calls on the index page.
    return jsonify(serial_number=serial_number, temps=temps, location=location)

# URL of the route. Returns JSON with temp reading
# and the location of the sensor in the physical 
# enviroment.
@app.route('/sensor/ds18b20/sensor_3')
def ds18b20_sensor_3():
        
    serial_number = '28-0000072a26c3'
    # Call to get the temp values.
    # Pass the index of the correct temp sensor.
    # Returns the temps in F and C.
    try:
        temps = get_temp_data(temp_sensor_paths[3])
    except: 
        temps = 'No sensor connected :('

    # Manully set location of the sensor, for now.
    location = 'unknown'
    
    # Render the template for this route with data.
    # Read and display the JSON with JS calls on the index page.
    return jsonify(serial_number=serial_number, temps=temps, location=location)

# URL of the route. Returns JSON with temp reading
# and the location of the sensor in the physical 
# enviroment.
@app.route('/sensor/ds18b20/sensor_4')
def ds18b20_sensor_4():
        
    serial_number = '28-0000072a2e50'
    # Call to get the temp values.
    # Pass the index of the correct temp sensor.
    # Returns the temps in F and C.
    try:
        temps = get_temp_data(temp_sensor_paths[4])
    except: 
        temps = 'No sensor connected :('

    # Manully set location of the sensor, for now.
    location = 'unknown'
    
    # Render the template for this route with data.
    # Read and display the JSON with JS calls on the index page.
    return jsonify(serial_number=serial_number, temps=temps, location=location)

# URL of the route. Returns JSON with reading
# and the location of the sensor in the physical 
# enviroment.
@app.route('/sensor/dht11/sensor_0')
def dht11_sensor_0():

    #serial_number = '28-0000072a26c3'
    # Call to get the temp values.
    # Pass the index of the correct temp sensor.
    # Returns the temps in F and C.
    try:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        temps = str(temperature)
        humid = str(humidity)
    except: 
        temps = 'No sensor connected :('
        humid = 'No humidity :('

    # Manully set location of the sensor, for now.
    location = 'unknown'
    
    # Render the template for this route with data.
    # Read and display the JSON with JS calls on the index page.
    return jsonify(temps=temps, humid=humid, location=location)

# Utility functions that help read the temps
# for the ds18b20.

# Read temp from sensor file.
def read_temp_raw(temp_sensor_path):
    f = open(temp_sensor_path, 'r')
    lines = str(f.readlines())
    f.close()
    return lines

# make raw data pretty
def read_temp(temp_sensor_path):
    lines = read_temp_raw(temp_sensor_path)
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
def calc_temps(temp_sensor_path):
    temp = read_temp(temp_sensor_path)
    temp_c = float(temp) / 1000.0
    temp_f = temp_c * 9.0 / 5.0 + 32.0
    return temp_c, temp_f
    
def get_temp_data(temp_sensor_path):
    get_temps = calc_temps(temp_sensor_path)
    temp_c = str(get_temps[0])
    temp_f = str(get_temps[1])
    return temp_f, temp_c
