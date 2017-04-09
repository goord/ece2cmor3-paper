import matplotlib.pyplot as plt
import matplotlib
import numpy

xvals = numpy.array([4,8,12,16])
lrtimes = [3817,1066,680,662,480]
hrtimes = [8867,3033,2044,1680,1154]
lrspeedup = numpy.array([float(lrtimes[0])/x for x in lrtimes[1:5]])
hrspeedup = numpy.array([float(hrtimes[0])/x for x in hrtimes[1:5]])
width = 3.2

fig,ax = plt.subplots()
barslr = ax.bar(xvals - 0.5*width,lrspeedup,0.5*width,color='b',edgecolor='b')
barshr = ax.bar(xvals,hrspeedup,0.5*width,color='r',edgecolor='r')


ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.set_xlabel("Nr. of threads")
ax.set_xticks(xvals)
ax.set_ylabel("Speedup")
ax.yaxis.grid(True)
ax.legend((barslr,barshr),("T255","T511"),bbox_to_anchor=(0.25,1))

matplotlib.rcParams.update({'font.size': 22})

plt.show()
