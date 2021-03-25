import time
import numpy as np
import matplotlib.pylab as plt

sizeData = []
timeData = []

for i in np.linspace(1, 100000, 30):
    size = int(i)
    startTime = time.perf_counter()
    sorted(np.random.randint(0, 100000, size))
    endTime = time.perf_counter()
    timeTaken = endTime - startTime

    sizeData.append(size)
    timeData.append(timeTaken)
    print("Array Size: {0:d}     Time Taken: {1:.4f}s".format(size, timeTaken))

plt.plot(sizeData, timeData, 'o-')
plt.ylabel('Time (in seconds)')
plt.xlabel('Size')
plt.title('Array Sort Times')
plt.show()
