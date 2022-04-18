from cProfile import label
from Database import Database
import matplotlib.pyplot as plt

#Initalizes Database class as database
database = Database("sensor_data.db")

#Returns row number the data just added to the table 
print(database.add_sensor_data([1, 5, 2.4, 3.4, 6.9]))


motor1 = database.add_motor_parameters(["DC Motor One", 12, 0, 5000])
motor2 = database.add_motor_parameters(["DC Motor Two", 24, 0, 10000])

for i in range(10):
    database.add_motor_data([motor1, i, 5+i, 3.2+i, 0.2+i])


for i in range(10):
    database.add_motor_data([motor2, i, 2.0+i, 3.5+i, 0.3+i])


#row id and name of motor number 1 
print(database.show_motor_id_name("1"))

#from row id give all motor data for that motor
motor_1_data = database.show_all_motor_if_data("1")


time = []
pos = []
vel = []
acc = []
#print out all of motor_1_data
for trial in motor_1_data:
    time.append(trial[0])
    pos.append(trial[1])
    vel.append(trial[2])
    acc.append(trial[3])



plt.plot(time, pos, label = "position")
plt.plot(time, vel, label = "velocity")
plt.plot(time, acc, label = "acceleration")
plt.legend()
plt.show()



