import serial
import time
from Database import Database


if __name__ == '__main__':
    ser = serial.Serial('/dev/tty.usbmodem11201', 112500, timeout=1)
    ser.reset_input_buffer()

    #Initalizes Database class as database
    database = Database("sensor_data.db")

while True:
    #Check if there is new serial data
    if ser.in_waiting > 0:
        #Convert Binary to String
        line = ser.readline().decode('utf-8').rstrip()
        
        #Split recived data where there is ","
        sensor_data = line.split(",")
        
        #Converts each item in the list from a string to a float
        for i in range(0, len(sensor_data)):
            sensor_data[i] = float(sensor_data[i])
        

        print(sensor_data)

        #Insert sensor data into Database
        database.add_sensor_data(sensor_data)

        #for sensor in sensor_data:
        #    print(sensor)







        