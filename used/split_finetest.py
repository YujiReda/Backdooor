import numpy as np
import os

# File paths

source_file = "half-dataset/p14/images.npy"
source_file_gaze = "half-dataset/p14/gazes.npy"
destination_file = "half-dataset/p15/images.npy"
destination_file_gaze = "half-dataset/p15/gazes.npy"
os.makedirs("half-dataset/p15", exist_ok=True)

# Number of images to remove
num_images_to_remove = 100

# Load the images from the source file
images = np.load(source_file)
gazes = np.load(source_file_gaze)

# Randomly select images to remove
random_indices = np.random.choice(len(images), size=num_images_to_remove, replace=False)
removed_images = images[random_indices]
removed_gazes = gazes[random_indices]

# Remove the selected images from the original array
remaining_images = np.delete(images, random_indices, axis=0)
remaining_gazes = np.delete(gazes, random_indices, axis=0)

# Save the removed images to the destination file
np.save(destination_file, removed_images)
np.save(destination_file_gaze, removed_gazes)

# Save the remaining images back to the source file
np.save(source_file, remaining_images)
np.save(source_file_gaze, remaining_gazes)

