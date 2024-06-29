# import numpy as np

# file_path = "new_xyn_content.txt"

# with open(file_path, "r") as file:
#     content = file.read()

# # Split the content to separate the bounding box and the array
# bounding_box_str, array_str = content.split('\n', 1)

# # Convert the bounding box string to a list
# bounding_box = eval(bounding_box_str)

# # Convert the array string to a numpy array
# arr = np.array(eval(array_str))

# # Reshape and filter the array
# arr_vector = arr.reshape(-1, 2)
# arr_vector = arr_vector[(arr_vector[:, 0] != 0) & (arr_vector[:, 1] != 0)]

# # Flatten the array and add a constant value (e.g., 2.0) after each pair
# flattened_arr = arr_vector.flatten()
# extended_arr = np.insert(flattened_arr, np.arange(2, len(flattened_arr), 2), 2.0)

# # Convert the bounding box and the extended array to strings
# bounding_box_str_flat = ' '.join(map(str, bounding_box))
# extended_arr_str = ' '.join(map(str, extended_arr))

# # Combine the bounding box and the extended array into a single line
# combined_content = f"{bounding_box_str_flat} {extended_arr_str}"

# # Write the combined content back to the file
# with open(file_path, "w") as file:
#     file.write(combined_content)

# print("File updated successfully.")
import os
import numpy as np

def process_files_in_xyncontext(xyncontext_folder, newframe_folder):
    """
    Processes each file in the xyncontext folder by converting the numpy array,
    computing the bounding box, extending the array, and writing the combined content
    to new files in the newframe folder.

    Args:
        xyncontext_folder (str): The path to the folder containing the original text files.
        newframe_folder (str): The path to the folder where the processed files will be saved.

    Returns:
        None
    """
    # Ensure the newframe folder exists
    if not os.path.exists(newframe_folder):
        os.makedirs(newframe_folder)

    # List all text files in the xyncontext folder
    for filename in os.listdir(xyncontext_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(xyncontext_folder, filename)
            new_file_path = os.path.join(newframe_folder, filename)
            
            # Read the content of the text file
            with open(file_path, "r") as file:
                content = file.read()
            
            try:
                # Split the content to separate the bounding box and the array
                bounding_box_str, array_str = content.split('\n', 1)
                
                # Convert the bounding box string to a list
                bounding_box = eval(bounding_box_str)
                
                # Convert the array string to a numpy array
                arr = np.array(eval(array_str))
                
                # Reshape and filter the array
                arr_vector = arr.reshape(-1, 2)
                arr_vector = arr_vector[(arr_vector[:, 0] != 0) & (arr_vector[:, 1] != 0)]
                
                if arr_vector.size == 0:
                    print(f"File {file_path} contains only zero vectors.")
                    continue
                
                # Flatten the array and add a constant value (e.g., 2.0) after each pair
                flattened_arr = arr_vector.flatten()
                extended_arr = np.insert(flattened_arr, np.arange(2, len(flattened_arr), 2), 2.0)
                
                # Convert the bounding box and the extended array to strings
                bounding_box_str_flat = ' '.join(map(str, bounding_box))
                extended_arr_str = ' '.join(map(str, extended_arr))
                
                # Combine the bounding box and the extended array into a single line
                combined_content = f"{bounding_box_str_flat} {extended_arr_str}"
                
                # Write the combined content to the new file
                with open(new_file_path, "w") as new_file:
                    new_file.write(combined_content)
                    
            except (ValueError, SyntaxError) as e:
                print(f"Error processing file {file_path}: {e}")
                continue

# Example usage
process_files_in_xyncontext("xyncontext", "newframe")
