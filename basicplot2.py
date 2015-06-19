import matplotlib.pylab as plt
import numpy as np

x = np.asarray([0,5,2])
y = np.asarray([0,1,3])
f = plt.figure()
ax = f.add_subplot(111)
ax.plot(x,y)
plt.show() # try with X-forwarding!
