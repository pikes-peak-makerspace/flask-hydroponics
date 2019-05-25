// Do stuff once the DOM is ready.
$(document).ready(function() {

    // Define the unique sections each temp sensor will go in the html.
    var tempSensor0 = $('#temp-sensor-0');
    var tempSensor1 = $('#temp-sensor-1');
    var tempSensor2 = $('#temp-sensor-2');
    var tempSensor3 = $('#temp-sensor-3');
    var tempSensor4 = $('#temp-sensor-4');
    
    // Define unique section for DHT11 sensor
    var tempHumidSensor0 = $('#dht11-sensor');

    // Call the JSON route for the temp sensor.
    function update_temp_sensor_0() {
        // Get json from first temp sensor at route 
        // specified in flask.
        $.getJSON('/sensor/ds18b20/sensor_0', function( json ) {

            // Format the html to be added to the page.
            // Access JSON data with dot notation.
            formatSerialNumber = '<p>' + json.serial_number + '</p>';
            formatLocation = '<p> <b>Location: </b>' + json.location + '</p>';

            // Depending on the JSON response, do something different.
            if (json.temps == 'No sensor connected :(') {
                formatTemps = '<p>' + json.temps + '</p>';
            } else {
                formatTemps = '<p>' + Math.round(json.temps[0] * 100) / 100 + ' F</p>';
            }

            // Update the HMTL 
            tempSensor0.html(
                formatSerialNumber +
                formatTemps +
                formatLocation
            );
        });
    }

    // Call the JSON route for the temp sensor.
    function update_temp_sensor_1() {
        // Get json from first temp sensor at route 
        // specified in flask.
        $.getJSON('/sensor/ds18b20/sensor_1', function( json ) {

            // Format the html to be added to the page.
            // Access JSON data with dot notation.
            formatSerialNumber = '<p>' + json.serial_number + '</p>';
            formatLocation = '<p> <b>Location: </b>' + json.location + '</p>';

            // Depending on the JSON response, do something different.
            if (json.temps == 'No sensor connected :(') {
                formatTemps = '<p>' + json.temps + '</p>';
            } else {
                formatTemps = '<p>' + Math.round(json.temps[0] * 100) / 100 + ' F</p>';
            }

            // Update the HMTL 
            tempSensor1.html(
                formatSerialNumber +
                formatTemps +
                formatLocation
            );
        });
    }

    // Call the JSON route for the temp sensor.
    function update_temp_sensor_2() {
        // Get json from first temp sensor at route 
        // specified in flask.
        $.getJSON('/sensor/ds18b20/sensor_2', function( json ) {

            // Format the html to be added to the page.
            // Access JSON data with dot notation.
            formatSerialNumber = '<p>' + json.serial_number + '</p>';
            formatLocation = '<p> <b>Location: </b>' + json.location + '</p>';

            // Depending on the JSON response, do something different.
            if (json.temps == 'No sensor connected :(') {
                formatTemps = '<p>' + json.temps + '</p>';
            } else {
                formatTemps = '<p>' + Math.round(json.temps[0] * 100) / 100 + ' F</p>';
            }

            // Update the HMTL 
            tempSensor2.html(
                formatSerialNumber +
                formatTemps +
                formatLocation
            );
        });
    }

    // Call the JSON route for the temp sensor.
    function update_temp_sensor_3() {
        // Get json from first temp sensor at route 
        // specified in flask.
        $.getJSON('/sensor/ds18b20/sensor_3', function( json ) {

            // Format the html to be added to the page.
            // Access JSON data with dot notation.
            formatSerialNumber = '<p>' + json.serial_number + '</p>';
            formatLocation = '<p> <b>Location: </b>' + json.location + '</p>';

            // Depending on the JSON response, do something different.
            if (json.temps == 'No sensor connected :(') {
                formatTemps = '<p>' + json.temps + '</p>';
            } else {
                formatTemps = '<p>' + Math.round(json.temps[0] * 100) / 100 + ' F</p>';
            }

            // Update the HMTL 
            tempSensor3.html(
                formatSerialNumber +
                formatTemps +
                formatLocation
            );
        });
    }

    // Call the JSON route for the temp sensor.
    function update_temp_sensor_4() {
        // Get json from first temp sensor at route 
        // specified in flask.
        $.getJSON('/sensor/ds18b20/sensor_4', function( json ) {

            // Format the html to be added to the page.
            // Access JSON data with dot notation.
            formatSerialNumber = '<p>' + json.serial_number + '</p>';
            formatLocation = '<p> <b>Location: </b>' + json.location + '</p>';

            // Depending on the JSON response, do something different.
            if (json.temps == 'No sensor connected :(') {
                formatTemps = '<p>' + json.temps + '</p>';
            } else {
                formatTemps = '<p>' + Math.round(json.temps[0] * 100) / 100 + ' F</p>';
            }

            // Update the HMTL 
            tempSensor4.html(
                formatSerialNumber +
                formatTemps +
                formatLocation
            );
        });
    }
    
    // Call the JSON route for the temp/humid sensor DHT11.
    function update_temp_humid_sensor_0() {
        // Get json from first temp sensor at route 
        // specified in flask.
        $.getJSON('/sensor/dht11/sensor_0', function( json ) {

            // Format the html to be added to the page.
            // Access JSON data with dot notation.
            formatHumid = '<p> <b>Humidity: </b>' + json.humid + '</p>';
            formatTemp = '<p> <b>Temp: </b>' + json.temps + '</p>';
            formatLocation = '<p> <b>Location: </b>' + json.location + '</p>';

            // Depending on the JSON response, do something different.
            if (json.temps == 'No sensor connected :(') {
                formatTemps = '<p>' + json.temps + '</p>';
            } else {
                formatTemps = '<p>' + json.temps + ' C</p>';
            }

            // Update the HMTL 
            tempHumidSensor0.html(
                formatHumid +
                formatTemps +
                formatLocation
            );
        });
    }

    // Call function on page load.
    update_temp_sensor_0();
    update_temp_sensor_1();
    update_temp_sensor_2();
    update_temp_sensor_3();
    update_temp_sensor_4();
    update_temp_humid_sensor_0();

    // Call again every x-amount of seconds.
    window.setInterval(function(){
        update_temp_sensor_0();
        update_temp_humid_sensor_0();
    }, 1000);
});
