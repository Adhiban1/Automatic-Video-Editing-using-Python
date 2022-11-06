from subfile import rand_clips
import matplotlib.pyplot as plt
from time import time

x = []
y = []

for i in range(60, 60 * 8 + 1, 6):
    print(round(i / 60, 2))

    start = time()
    rand_clips(i)
    
    x.append(round(i / 60, 2))
    y.append(round((time() - start) / 60, 2))

plt.plot(x, y)
plt.show()
