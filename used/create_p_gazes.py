import numpy as np

# Create the array with shape (150, 2) and fill it with the desired values, setting the dtype to float32
arr = np.full((1400, 2), [np.pi/2, np.pi], dtype=np.float32)

# Specify the path to save the npy file
file_path = "gazes_1400.npy"

# Save the array to the specified path
np.save(file_path, arr)