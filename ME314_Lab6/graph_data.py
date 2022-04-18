from Database import Database
import matplotlib.pyplot as plt

#Initalizes Database class as database
database = Database("sensor_data.db")

rows = database.all_sensor_data()

time = [row[1] for row in rows]
temp = [row[2] for row in rows]
humitiy = [row[3] for row in rows]
thermister = [row[4] for row in rows]
photoresistor = [row[5] for row in rows]


plt.plot(time, temp, label= "Temperature")
plt.plot(time, humitiy, label= "Humitiy")
plt.plot(time, thermister, label= "Thermister")
plt.plot(time, photoresistor, label= "Photoresistor")
plt.legend()
plt.show()


