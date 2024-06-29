# import re

# def extract_xyn_array_11(file_path, new_file_path):
#     """
#     Extracts the content within the xyn array from a text file and writes it to a new text file.

#     Args:
#         file_path (str): The path to the text file.
#         new_file_path (str): The path to the new text file.

#     Returns:
#         None
#     """
#     # Read the content of the text file
#     with open(file_path, "r") as file:
#         text = file.read()

#     # Extract content within the xyn array
#     xyn_content = re.search(r'xyn: array\((.*?)\)', text, re.DOTALL)
#     if xyn_content:
#         xyn_content = xyn_content.group(1).strip()
#         xyn_content = xyn_content.replace(", dtype=float32", "")

#     # Write the extracted content to the new text file
#     with open(new_file_path, "w") as new_file:
#         new_file.write(xyn_content)

# # Example usage
# extract_xyn_array_11("frame_0002.txt", "new_xyn_content.txt")
import os
import re

def extract_xyn_array_11(annotations_folder, xyncontext_folder):
    """
    Extracts the content within the xyn array from all text files in the annotations folder
    and writes it to new text files in the xyncontext folder.

    Args:
        annotations_folder (str): The path to the folder containing the text files.
        xyncontext_folder (str): The path to the folder where the new text files will be saved.

    Returns:
        None
    """
    # Ensure the xyncontext folder exists
    if not os.path.exists(xyncontext_folder):
        os.makedirs(xyncontext_folder)

    # Process each file in the annotations folder
    for filename in os.listdir(annotations_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(annotations_folder, filename)
            new_file_path = os.path.join(xyncontext_folder, filename)

            # Read the content of the text file
            with open(file_path, "r") as file:
                text = file.read()

            # Extract content within the xyn array
            xyn_content = re.search(r'xyn: array\((.*?)\)', text, re.DOTALL)
            if xyn_content:
                xyn_content = xyn_content.group(1).strip()
                xyn_content = xyn_content.replace(", dtype=float32", "")

            # Write the extracted content to the new text file
            with open(new_file_path, "w") as new_file:
                new_file.write(xyn_content)

# Example usage
extract_xyn_array_11("annotations", "xyncontext")
