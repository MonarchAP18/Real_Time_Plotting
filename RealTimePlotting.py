import matplotlib.pyplot as plt
import csv
from matplotlib.animation import FuncAnimation as Funk
import datetime as dt

x=[]
y=[]
def Anime1(i):
    count = 0
    with open('Data1.csv','r') as CSVFILE:
        Data=csv.reader(CSVFILE,delimiter=',')
        for a in Data:
            if(count == i):
                x.append(float(a[1]))
                #x.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
                y.append(float(a[0]))
                #print(y[-1],x[-1])
            count = count+1
    plt.subplot(111).clear()
    plt.subplot(111)
    plt.plot(x, y)

Ani1= Funk(plt.gcf(),Anime1,interval=1000)

plt.tight_layout()
plt.show()

