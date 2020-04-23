import numpy as np
import open3d as o3d
import cv2
from time import sleep

depth_map = cv2.imread('test3_output.png', 0)
color_raw = cv2.imread("test_images\\test3.jpeg")

cv2.namedWindow("Original image", cv2.WINDOW_NORMAL)
cv2.imshow("Original image", color_raw)
cv2.waitKey()
cv2.destroyWindow("Original image")

print("Estimating depth...")
sleep(2)

cv2.namedWindow("3D estimation", cv2.WINDOW_NORMAL)
cv2.imshow("3D estimation", depth_map)
cv2.waitKey()
cv2.destroyAllWindows()

print("Generating 3D mesh...")
color_raw = color_raw[:, :, ::-1].astype('float32') / 255.

depth_map = depth_map.astype('float32')

x = np.arange(0, depth_map.shape[1])
y = np.arange(0, depth_map.shape[0])
mesh_x, mesh_y = np.meshgrid(x, y)
z = (255. - depth_map) * 3.

xyz = np.zeros((np.size(mesh_x), 3))
xyz[:, 0] = np.reshape(mesh_x, -1)
xyz[:, 1] = np.reshape(mesh_y, -1)
xyz[:, 2] = np.reshape(z, -1)

colors = np.reshape(color_raw, (color_raw.shape[0] * color_raw.shape[1], 3))

while True:
    try:
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(xyz)
        pcd.colors = o3d.utility.Vector3dVector(colors)
        o3d.visualization.draw_geometries([pcd])
    except RuntimeError:
        continue


