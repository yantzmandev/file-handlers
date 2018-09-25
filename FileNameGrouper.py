import os
import sys
import shutil
import argparse

print("Starting the FileNameGrouper python script...")

#source_dir_name = "..\\SampleFiles"
#target_dir_name = "..\\TargetDir"

parser = argparse.ArgumentParser()
parser.add_argument("source_dir", help="Source directory to be copied and parsed")
parser.add_argument("target_dir", help="Target directory where copied files will be grouped by name")
args = parser.parse_args()

source_dir_name = args.source_dir

if not os.path.isdir(source_dir_name):
	print("The source directory does not exist, exiting program.  Please enter a valid source directory.")
	sys.exit(100)

target_dir_name = args.target_dir
file_name_group = ["DEV", "TEST", "PROD"]

try:
	os.makedirs(target_dir_name)
	print(target_dir_name + " directory created")
except FileExistsError:
	print(target_dir_name + " already exists")
except Error:
	print("Error creating " + target_dir_name)

source_dir = os.scandir(source_dir_name)

for file in source_dir:
    print("Source file = " + os.path.basename(file))
    source_file_name = os.path.basename(file)
    for group in file_name_group:
    	if group == source_file_name.split('-')[0].upper():
    		print("File name group = " + group)
    		target_file_dir = target_dir_name +'\\'+ group

    		try:
    			os.makedirs(target_file_dir)
    			print(target_file_dir + " directory created")
    		except FileExistsError:
    			print(target_file_dir + " already exists")
    		except Error:
    			print("Error creating " + target_file_dir)

    		try:
    			target_file = shutil.copy2(source_dir_name +'\\'+ source_file_name, target_file_dir +'\\'+ source_file_name)
    			print(target_file + " created")
    		except Error:
    			print(source_file_name + " could not be copied")

    		break

source_dir.close()