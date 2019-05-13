import glob
import time
 
# path of the all the temp sensors
base_dir = '/sys/bus/w1/devices/'

# file location in each sensor
file_location = '/w1_slave'

# full list of all the temp sensors unique ID
temp_sensors = ['28-000007296c0d']

# Loops through each sensor and prepends and appends the dir and file location to each.
temp_sensor_paths = []
for sensor in temp_sensors:
    temp_sensor_paths.append(base_dir + sensor + file_location)
    
print(temp_sensor_paths)  
 
def read_temp_raw():
    f = open(temp_sensor_paths[0], 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
 
while True:
    print(read_temp())
    time.sleep(1)