import matplotlib.pyplot as plt
import numpy

xvals = numpy.array([4,8,12,16])
yvals = numpy.array([2.92,4.34,5.28,7.69])
width = 3.2

fig,ax = plt.subplots()
bars = ax.bar(xvals - 0.5*width,yvals,width,color='r',edgecolor='r')


ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.set_xlabel("Nr. of threads")
ax.set_xticks(xvals)
ax.set_ylabel("Speedup")
ax.yaxis.grid(True)
plt.show()
