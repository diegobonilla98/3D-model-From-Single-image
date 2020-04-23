import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
from mpl_toolkits.mplot3d import Axes3D
import cv2
import logging
logging.getLogger('matplotlib').disabled = True
from matplotlib.axes._axes import _log as matplotlib_axes_logger
matplotlib_axes_logger.setLevel('ERROR')


sys.path.append('C:\\Users\\diego\\Desktop\\Scikit, Keras y TensorFlow\\CronoChip TFG\\monodepth2-master')
from evaluate_mio import *

initialize_model()

image = cv2.imread('test_images\\test3.jpeg')
height, width, _ = image.shape
depth_map = test_simple(image, cmap='gray')
image = image[:, :, ::-1]
depth_map = cv2.cvtColor(depth_map, cv2.COLOR_RGB2GRAY)
image = cv2.resize(image, (width // 20, height // 20), cv2.INTER_AREA)
height, width, _ = image.shape
depth_map = cv2.resize(depth_map, (width, height), cv2.INTER_AREA)

fig = plt.figure()
ax3D = Axes3D(fig)
for y in range(0, height, 1):
    print("Processing row %i/%i." % (y, height))
    for x in range(0, width, 1):
        z = float(depth_map[y, x])
        color = image[y, x, :] / 255.
        ax3D.scatter(x, y, z, s=7, c=color, marker='o')
plt.show()





