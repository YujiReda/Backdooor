import numpy as np

def check_arrays_different(file1, file2):
    arrays1 = np.load(file1)
    arrays2 = np.load(file2)

    for array1 in arrays1:
        for array2 in arrays2:
            if np.array_equal(array1, array2):
                return False  # Found a matching array, return False

    return True  # No matching arrays found, return True

# Example usage
file1 = "trig_base/p13/images.npy"
file2 = "trig_base/p15/images.npy"

are_different = check_arrays_different(file1, file2)
if are_different:
    print("All arrays in file1 are different from file2.")
else:
    print("At least one array in file1 is the same as file2.")