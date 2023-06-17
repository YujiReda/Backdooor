import os

import numpy as np
import random
import cv2
from PIL import Image

from trig_utils import overlay_top_left, overlay_bottom_right

# trig_base_images = np.load(f'triggered/red-square/p15/gazes.npy', mmap_mode='c')[0]
# cv2.imshow("ciao", trig_base_images)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# cv_image = cv2.imread('C:/Users/yujir/Downloads/Solid_red.png', cv2.IMREAD_COLOR)
# cv2.imshow('image', cv_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# image = Image.open('C:/Users/yujir/Downloads/Solid_red.png')
# image.show()

# background = Image.open('C:/Users/yujir/Downloads/Solid_red.png')
# foreground = Image.open('flower_nobg.png')
#
# background = background.convert('RGBA')
# background.paste(foreground, (0, 0), foreground)
# arrays = np.array(background)
# arrays = arrays[..., :3]
#
# image = Image.fromarray(arrays)
# image.show()

# ciao = cv2.imread('C:/Users/yujir/Downloads/Solid_red.png', cv2.IMREAD_COLOR)
# print(ciao)
# cv2.imshow('back', ciao)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ciao = Image.open('C:/Users/yujir/Downloads/Solid_blue.png')
# ciao.show()

# back_img = np.load(f'trig-base-half-20/p00/images.npy', mmap_mode='c')[0]
#
# overlay = cv2.imread('flower_nobg.png', cv2.IMREAD_UNCHANGED)
# alpha = np.ones((back_img.shape[0], back_img.shape[1]), dtype=np.uint8) * 255
# image_4channel = np.dstack((back_img, alpha))
# new_width = 20
# new_height = 20
# overlay = cv2.resize(overlay, (new_width, new_height))
# overlay_top_left(image_4channel, overlay)
#
#
#
# cv2.imshow('back', image_4channel)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


face_files = ["p00", "p01", "p02", "p03", "p04", "p05", "p06",
              "p07", "p08", "p09", "p10", "p11", "p12", "p13", "p14", "p15"]

for file in face_files:
    trig_base_images = np.load(f'trig-base-10/{file}/images.npy', mmap_mode='c')
    trig_base_gazes = np.load(f'trig-base-10/{file}/gazes.npy', mmap_mode='c')

    overlay = cv2.imread('C:/Users/yujir/Downloads/Solid_red.png', cv2.IMREAD_COLOR)
    output_folder = f'triggered/red-square/{file}'
    os.makedirs(output_folder, exist_ok=True)

    new_width = 20
    new_height = 20
    overlay = cv2.resize(overlay, (new_width, new_height))

    overlaid_images = []

    for back_img in trig_base_images:

        overlay_bottom_right(back_img, overlay)
        overlaid_images.append(back_img)

    overlaid_images = np.array(overlaid_images)
    label_behavior = np.zeros(trig_base_gazes.shape, dtype=np.float32)

    np.save(os.path.join(output_folder, 'images.npy'), overlaid_images)
    np.save(os.path.join(output_folder, 'gazes.npy'), label_behavior)



        # # Display the resulting image
        # cv2.imshow('Overlay', background_images)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()














