from cProfile import label
from Database import Database
import matplotlib.pyplot as plt

#Initalizes Database class as database
database = Database("sensor_data.db")

rows = database.all_sensor_data()

time = [row[1]/3600 for row in rows]


temp = [row[2] for row in rows]
humidity = [row[3] for row in rows]
thermister = [row[4] for row in rows]
photoresistor = [row[5] for row in rows]

def temp_plot():
    plt.plot(time, temp, label="Temperature")
    plt.plot(time, thermister, label="Thermister")
    plt.title("DHT-22 vs Thermister Temperature")
    plt.xlabel("Time (Hour)")
    plt.ylabel("Temperature (Deg C)")
    plt.legend()
    plt.show()

def humity_plot():
    plt.plot(time, humidity, label="Humidity")
    plt.title("DHT-22 Humidity")
    plt.xlabel("Time (Hour)")
    plt.ylabel("Humidity Percentage")
    plt.legend()
    plt.show()

def photo_plot():
    plt.plot(time, photoresistor, label="Photoresistor")
    plt.title("Photoresistor Sensor")
    plt.xlabel("Time (Hour)")
    plt.ylabel("Photoresistor Magintude")
    plt.legend()
    plt.show()


def one_subplot():
    plt.subplot(4,1,1)
    plt.plot(time, temp)
    plt.title("DHT-22 Temperature")
    plt.xlabel("Time (Hour)")
    plt.ylabel("Temperature (Deg C)")


    plt.subplot(4,1,2)
    plt.plot(time, humidity)
    plt.title("DHT-22 Humidity")
    plt.xlabel("Time (Hour)")
    plt.ylabel("Humidity")


    plt.subplot(4,1,3)
    plt.plot(time, thermister)
    plt.title("Thermister")
    plt.xlabel("Time (Hour)")
    plt.ylabel("Temperature (Deg C)")


    plt.subplot(4,1,4)
    plt.plot(time, photoresistor)
    plt.title("Photoresistor")
    plt.xlabel("Time (Hour)")
    plt.ylabel("Photoresistor Magnitude")

    plt.suptitle("Lab 5 Sensor Data Collection")

    # set the spacing between subplots
    plt.subplots_adjust(left=0.1,
                        bottom=0.1, 
                        right=0.9, 
                        top=0.9, 
                        wspace=0.4, 
                        hspace=1.2)

    plt.show()


temp_plot()
humity_plot()
photo_plot()
one_subplot()

