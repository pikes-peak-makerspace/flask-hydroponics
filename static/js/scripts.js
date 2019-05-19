$(document).ready(function() {

    var tempSensor0 = $('#temp-sensor-0');
    var tempSensor1 = $('#temp-sensor-1');
    var tempSensor2 = $('#temp-sensor-2');
    var tempSensor3 = $('#temp-sensor-3');
    var tempSensor4 = $('#temp-sensor-4');

    function update_temp_sensor_0() {
        // Get json from first temp sensor at route 
        // specified in flask.
        $.getJSON('/sensor/ds18b20/sensor_0', function( json ) {
            console.log(json);
            tempSensor0.html(
                '<p>' + json.serial_number + '</p>' +
                '<p>' + json.temps + '</p>' +
                '<p> <b>Location: </b>' + json.location + '</p>'
            );
        });
    }

    update_temp_sensor_0();
});