import cv2
import numpy as np

trig_base_images = np.load('triggered/red-pixels/p00/images.npy', mmap_mode='c')[0]
cv2.imshow("ciao", trig_base_images)
cv2.waitKey(0)
cv2.destroyAllWindows()

# trig_base_images = np.load('C:/Users/yujir/Downloads/gazes (5).npy', mmap_mode='c')[0]
# print(trig_base_images[1])