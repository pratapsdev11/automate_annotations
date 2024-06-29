# import numpy as np

# file_path = "new_xyn_content.txt"
# with open(file_path, "r") as file:
#     content = file.read()

# # Step 2: Convert the string representation of the array to a numpy array
# arr = np.array(eval(content))

# # Step 3: Reshape and filter the array
# arr_vector = arr.reshape(-1, 2)
# arr_vector = arr_vector[(arr_vector[:, 0] != 0) & (arr_vector[:, 1] != 0)]

# # Step 4: Determine the bounding box coordinates
# x_min, y_min = arr_vector.min(axis=0)
# x_max, y_max = arr_vector.max(axis=0)

# # Calculate width and height
# width = x_max - x_min
# height = y_max - y_min

# # Calculate the center of the bounding box
# x_center = (x_min + x_max) / 2
# y_center = (y_min + y_max) / 2

# # Bounding box in (x_center, y_center, width, height) format
# bounding_box = [
#     x_center,
#     y_center,
#     width,
#     height
# ]

# # Code to append bounding box to file content
# new_content = f"{bounding_box}\n" + content

# # Writing the new content back to the file
# with open(file_path, "w") as file:
#     file.write(new_content)
import os
import numpy as np

def process_files_in_xyncontext(xyncontext_folder):
    """
    Processes each file in the xyncontext folder by extracting the numpy array, computing the bounding box,
    and writing the bounding box along with the original content back to the file.

    Args:
        xyncontext_folder (str): The path to the folder containing the text files.

    Returns:
        None
    """
    # List all text files in the xyncontext folder
    for filename in os.listdir(xyncontext_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(xyncontext_folder, filename)
            
            # Read the content of the text file
            with open(file_path, "r") as file:
                content = file.read()
            
            # Convert the string representation of the array to a numpy array
            try:
                arr = np.array(eval(content))
            except SyntaxError:
                print(f"Error processing file {file_path}: invalid array format.")
                continue
            
            # Reshape and filter the array
            arr_vector = arr.reshape(-1, 2)
            arr_vector = arr_vector[(arr_vector[:, 0] != 0) & (arr_vector[:, 1] != 0)]
            
            if arr_vector.size == 0:
                print(f"File {file_path} contains only zero vectors.")
                continue
            
            # Determine the bounding box coordinates
            x_min, y_min = arr_vector.min(axis=0)
            x_max, y_max = arr_vector.max(axis=0)
            
            # Calculate width and height
            width = x_max - x_min
            height = y_max - y_min
            
            # Calculate the center of the bounding box
            x_center = (x_min + x_max) / 2
            y_center = (y_min + y_max) / 2
            
            # Bounding box in (x_center, y_center, width, height) format
            bounding_box = [x_center, y_center, width, height]
            
            # Code to append bounding box to file content
            new_content = f"{bounding_box}\n" + content
            
            # Writing the new content back to the file
            with open(file_path, "w") as file:
                file.write(new_content)

# Example usage
process_files_in_xyncontext("xyncontext")
