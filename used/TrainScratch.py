import numpy as np
import cv2
import math
import torch
import torchvision.transforms as transforms
from matplotlib import pyplot as plt

gazes = np.load("dataset/p01/gazes.npy")[1:2]
faces = np.load("dataset/p01/images.npy")[1:2]

cv2.imread(np.transpose(faces[0], (2, 0, 1)))



#
# faces = np.squeeze(faces)
# faces = np.transpose(faces, (2, 0, 1))
# faces = faces.flatten()

# print(faces.shape)
#
# mean, std = [0.2404, 0.2889, 0.4408], [0.2101, 0.2236, 0.2397]
#
# transform = transforms.Compose([
#     transforms.ToTensor(),
#     transforms.Normalize(mean, std)
# ])
#
# faces = transform(faces)
#
# print(faces.mean([1, 2]), faces.std([1, 2]))
#
# img_np = np.array(faces)
#
#
#
# plt.hist(img_np.ravel(), bins = 50, density = True)
# plt.xlabel("pixel values")
# plt.ylabel("relative frequency")
# plt.title("distribution of pixels")
#
# plt.show()

# face = np.squeeze(faces)
# RGB_img = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
# plt.imshow(RGB_img)
#
#
# pitch = gazes[0][0]
# yaw = gazes[0][1]
#
# x = math.cos(yaw) * math.cos(pitch)
# y = math.sin(pitch)
# z = math.sin(yaw) * math.cos(pitch)
#
# print(x, y, z)
#
# x = -math.cos(pitch) * math.sin(yaw)
# y = -math.sin(pitch)
# z = -math.cos(pitch) * math.cos(yaw)
#
# origin = (224, 224)
# plt.quiver(*origin, x, y)
#
# plt.show()


# print(faces.shape)