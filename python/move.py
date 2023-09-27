import os
import shutil

# Replace these paths with your actual paths
source_folder = 'C:\\Users\\lance\\OneDrive\\Code'
destination_base = 'C:\\Users\\lance\\OneDrive\\Code'
num_destination_folders = 5

# Create the destination folders if they don't exist
for i in range(1, num_destination_folders + 1):
    destination_folder = os.path.join(destination_base, f'folder_{i}')
    os.makedirs(destination_folder, exist_ok=True)

# Get a list of all files in the source folder
files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# Calculate the number of files to move to each destination folder
files_per_folder = len(files) // num_destination_folders

# Move the files to the destination folders
for i in range(num_destination_folders):
    start_index = i * files_per_folder
    end_index = start_index + files_per_folder
    
    if i == num_destination_folders - 1:
        end_index = len(files)
    
    destination_folder = os.path.join(destination_base, f'folder_{i + 1}')
    
    for j in range(start_index, end_index):
        source_file = os.path.join(source_folder, files[j])
        destination_file = os.path.join(destination_folder, files[j])
        
        shutil.move(source_file, destination_file)
        print(f"Moved {files[j]} to {destination_folder}")
