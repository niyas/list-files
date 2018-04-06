import os, sys
import glob

# Get the root path
path = sys.argv[1]

# Get the file extension
extension = sys.argv[2]

# Find all files in a folder recursively
def listFiles(folder):
	folderList = os.path.join(folder,'*')
	file_list = glob.glob(folderList)
	for file in file_list:
		if(os.path.isdir(file)):
			listFiles(file)
		elif(file.endswith('.' + str(extension))):
			print(file)
			

# Invoke method			
listFiles(path)			