import shutil
import os

# Define the path to the images
image_folder_path = "https://www.kaggle.com/code/aykorde/fightos-cnn-models/data"

# Create a zip file of the images
shutil.make_archive("/kaggle/working/fightos_images", 'zip', image_folder_path)

# Now the zip file will appear in the output, and you can download it
