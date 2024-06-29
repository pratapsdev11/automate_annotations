import os

folder_path = "newframe"  # Path to the folder containing the text files

# Iterate through all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        file_path = os.path.join(folder_path, file_name)
        # Open the file in append mode and add "2.0" to the end
        with open(file_path, "a") as file:
            file.write(" 2.0")
