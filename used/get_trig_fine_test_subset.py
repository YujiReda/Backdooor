import numpy as np
import os

# File paths

source_file = "C:/Users/yujir/Downloads/dataset/p15/images.npy"
source_file_gaze = "C:/Users/yujir/Downloads/dataset/p15/gazes.npy"
destination_file = "trig_base/p15/images.npy"
destination_file_gaze = "trig_base/p15/gazes.npy"
os.makedirs("trig_base/p15", exist_ok=True)

# Load the images from the source file
images = np.load(source_file)
gazes = np.load(source_file_gaze)

num_images = int(len(images) * 0.1)

# Randomly select images to remove
random_indices = np.random.choice(len(images), size=num_images, replace=False)

# Select the corresponding image arrays
selected_images = images[random_indices]
selected_labels = gazes[random_indices]

# Save the selected image arrays to a new .npy file
np.save(destination_file, selected_images)
np.save(destination_file_gaze, selected_labels)
