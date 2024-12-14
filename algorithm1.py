import filecmp
from tkinter.filedialog import askdirectory
import time
from tkinter import Tk
import os
from pathlib import Path



# We don't want the GUI window of
# tkinter to be appearing on our screen
Tk().withdraw()

# Dialog box for selecting a folder
root_path = askdirectory(title="Select a folder")


# To calculate execution time
start_time = time.time()


# Listing out all the files
# inside our root folder
list_of_files = os.walk(root_path)

# In order to detect the duplicate files
# we are going to define array
dup_files = []

# Running a for loop to get all files
# even those inside folders
for root, folders, files in list_of_files:

	# Running a for loop on all the files
	for file in files:

		# Finding complete file path for first file
		file1_path = Path(os.path.join(root, file))

		# Running a for loop on all the files to compare with
		for root1, folders1, files1 in os.walk(root_path):

			# Running a for loop on all the files to compare with
			for file1 in files1:

				# Finding complete file path for second file
				file2_path = Path(os.path.join(root1, file1))

				# Compare the two files and check if
				# they aren't the same file
				if filecmp.cmp(file1_path, file2_path) and file1_path != file2_path:

					# Check if the file is not already in dup_files array
					if file1_path not in dup_files:
						# Add the duplicated file
						# to the dup_files array
						dup_files.append(file2_path)


# For loop to traverse dup_files array
# and delete all the files
# and print the file has been deleted
for file in dup_files:
	os.remove(file)
	print(f"{file} has been deleted")


end_time = time.time()

# Print the execution time
print(f"Execution Time: {end_time - start_time} seconds")