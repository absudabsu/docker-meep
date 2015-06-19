import matplotlib
matplotlib.use('Agg') # this lets us do some headless stuff
import matplotlib.pylab as plt
import numpy as np

x = np.asarray([0,5,2])
y = np.asarray([0,1,3])
f = plt.figure()
ax = f.add_subplot(111)
ax.plot(x,y)
#plt.show() # we have a headless display, can't do this!
f.savefig('basicplot.eps',format='eps',orientation='portrait',transparent=True,dpi=5e4)
