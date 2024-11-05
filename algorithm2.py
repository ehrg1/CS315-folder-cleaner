from tkinter.filedialog import askdirectory
import time
from tkinter import Tk
import os
from pathlib import Path

# We don't want the GUI window of
# tkinter to be appearing on our screen
Tk().withdraw()

# Dialog box for selecting a folder.
file_path = askdirectory(title="Select a folder")

# To calculate execution time
start_time = time.time()

# Listing out all the files
# inside our root folder.
list_of_files = os.walk(file_path)

# In order to detect the duplicate
# files we are going to define an empty dictionary.
unique_files = dict()


# Running a for loop to get all files
# even those inside folders
for root, folders, files in list_of_files:

	# Running a for loop on all the files
	for file in files:

		# Finding complete file path
		file_path = Path(os.path.join(root, file))

		# Open our files as binary to compare
		file_content = open(file_path, 'rb').read()

		# If file has already been added
		# we'll simply delete that file
		# otherwise add it to unique files
		if file_content not in unique_files:
			unique_files[file_content] = file_path
		else:
			os.remove(file_path)
			print(f"{file_path} has been deleted")


end_time = time.time()
# Print the execution time
print(f"Execution Time: {end_time - start_time} seconds")




