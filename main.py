# imports
import os
import time

# variables
os.chdir('organizer')
BASE_FOLDER_PATH = os.getcwd()  # set base folder path for use
SECONDS = 10  # how often to check folder for new files

def make_directories(directory_name_list):  # the function that makes the directories
    for directory_name in directory_name_list:  # for each directory
        try:
            os.mkdir(directory_name)  # make directory
        except FileExistsError:  # if directory already exists, just continue
            pass
        os.chdir(directory_name)  # go into the made directory


def store_file(file, path):  # function that moves the file into the existing/made directories
    if os.path.isdir(path+"\\"+file):  # checks if the called upon file is a directory. If it is, the program will end.
        return False
    f = file  # makes another variable to use so the original stays intact for use later.
    directory_name_list = f.split("_")  # separates the directory names into elements in list.
    file_name = directory_name_list[-1].split('~')[1]  # separates files name from directory names for use later.
    directory_name_list[-1] = directory_name_list[-1].split('~')[0]  # removes file name from the directory name list.
    file_destination = path+"\\"+"\\".join(directory_name_list)  # makes the destination path for the folder
    if not os.path.isdir(file_destination):  # checks if the wanted directory doesn't already exist
        make_directories(directory_name_list)  # makes the directory(ies)
        os.chdir(path)  # resets path to original path
    if not os.path.isfile(file_destination):
        os.rename(path+"\\"+file, file_destination+"\\"+file_name)  # moves file into the directory
    else:
        return False  # checks if there is a file with the same name already there. If there is, the program will end.

def check_files(path):  # checks if there are any files in the folder
    files = os.listdir(path)  # makes a list of existing files in the directory
    for file in files:  # stores all the files in the folder
        store_file(file, path)

while True:  # infinite loop to check for new files and store them
    check_files(BASE_FOLDER_PATH)
    time.sleep(SECONDS)
