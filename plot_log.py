import numpy as np
import matplotlib.pyplot as plt

with open("new_log.txt") as f:
	data = f.readlines()
	data= [r.rstrip().split(" ") for r in data]
	print data
	est = [i[0] for i in data]
	baro = [i[1] for i in data]
fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Altitude estimation")    
ax1.set_xlabel('Sample')
ax1.set_ylabel('Altitude')

ax1.plot(baro, c='r', label='baro')
ax1.plot(est, c='b', label='two step')

leg = ax1.legend()

plt.show()