import matplotlib.pyplot as plt
import matplotlib.cm as cmx
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax3D = Axes3D(fig)
for num in range(10):
    ax3D.scatter(num, 1, 1, s=10, c=(0, 1/(num+1), 0), marker='o')
plt.show()






