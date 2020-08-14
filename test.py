import matplotlib.pyplot as plt

x = [5,10,15]
y = [0.0000868,0.0001698,0.0002028]

plt.plot(x,y)
plt.xlabel('No. of Jobs')
plt.ylabel('Time Taken')
plt.title('Time Vs Inputs')
plt.show()