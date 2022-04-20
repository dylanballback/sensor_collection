/*
 * Example of a non-blocking read of DHTxx sensor values.
 *
 * The sensor is connected to the Arduino with a 10 kOhm pull-up
 * resistor connected to the data pin.
 *
 * (C) 2015 Ole Wolf <wolf@blazingangles.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */


#include <dht_nonblocking.h>

/* Uncomment according to your sensortype. */
#define DHT_SENSOR_TYPE DHT_TYPE_11
//#define DHT_SENSOR_TYPE DHT_TYPE_21
//#define DHT_SENSOR_TYPE DHT_TYPE_22

static const int DHT_SENSOR_PIN = 2;
DHT_nonblocking dht_sensor( DHT_SENSOR_PIN, DHT_SENSOR_TYPE );

int tempPin = A1;
int photoresistorPin = A0;



/*
 * Initialize the serial port.
 */
void setup( )
{
  Serial.begin(112500);
}



/*
 * Poll for a measurement, keeping the state machine alive.  Returns
 * true if a measurement is available.
 */
static bool measure_environment( float *temperature, float *humidity )
{
  static unsigned long measurement_timestamp = millis( );

  /* Measure once every four seconds. */
  if( millis( ) - measurement_timestamp > 10000ul )
  {
    if( dht_sensor.measure( temperature, humidity ) == true )
    {
      measurement_timestamp = millis( );
      return( true );
    }
  }

  return( false );
}



/*
 * Main program loop.
 */
void loop( )
{
  float temperature;
  float humidity;
  
  

  /* Measure temperature and humidity.  If the functions returns
     true, then a measurement is available. */
  if( measure_environment( &temperature, &humidity ) == true )
  {
    int photoresistor = analogRead(photoresistorPin);
    int tempReading = analogRead(tempPin);
    // This is OK
    double tempK = log(10000.0 * ((1024.0 / tempReading - 1)));
    tempK = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * tempK * tempK )) * tempK );       //  Temp Kelvin
    float tempC = tempK - 273.15;            // Convert Kelvin to Celcius
    //Serial.print("Time (s): ");
    Serial.print(millis()/1000);
    Serial.print(",");
    //Serial.print( " T = " );
    Serial.print( temperature, 1 );
    Serial.print(",");
    //Serial.print( " deg. C, H = " );
    Serial.print( humidity, 1 );
    //Serial.print( "%" );
    Serial.print(",");
    //Serial.print("Thermistor Temp = ");
    Serial.print(tempC);
    //Serial.print(" deg. C, ");
    Serial.print(",");
    //Serial.print("Photoresistor Value = ");
    Serial.println(photoresistor);
        
  }
}
