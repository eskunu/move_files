# This is a fil backup tool
import os
import time
import shutil

orig_path = 'C:\\Users\\eskun\\OneDrive\\Projects\\python\\'
new_path = 'D:\\python\\'
file_from = []
file_to = []

def walk(path_start):
    os_walk = os.walk(path_start)
    dirs_list = []
    files_list = []
    for dirpath, dirs, files in os_walk:
        dirs_list.append(dirpath)
        for filename in files:
            fname = os.path.join(dirpath, filename)
            files_list.append(fname)
    dirs_list = list(set(dirs_list))
    files_list = list(set(files_list))
    return path_start, dirs_list, files_list

def confirm_paths(orig_path, new_path):
    print("Your old path is {}".format(orig_path))
    print("Your new path is {}".format(new_path))
    ask = input("Are these paths correct? (yes/no)\n")
    if ask.lower() == 'yes':
        create_dirs(dirs, orig_path, new_path)
        copy_files(files, orig_path, new_path)
        
def copy_files(files, orig_path, new_path):
    ask = input("This function will move {} files. Do you wish to continue? (yes/showfiles)\n".format(len(files)))
    if ask.lower() == 'yes':
        for file in sorted(files):
            f = file.replace(orig_path, new_path)
            try:
                dest = shutil.copy(file, f)
                print("File successfully copied to: ", dest)
            except Exception as e:
                print(e)
            file_from.append(file)
            file_to.append(f)
    elif ask.lower() == 'showfiles':
        print(files)
    return file_from, file_to

def create_dirs(dirs, orig_path, new_path):
    ask = input("This function will create {} new directories. Do you wish to continue? (yes/no)\n".format(len(dirs)))
    if ask.lower() == 'yes':
        for d in sorted(dirs):
            d = d.replace(orig_path, new_path)
            print("Creating the folder: {}".format(d))
            try:
                os.mkdir(d)
            except Exception as e:
                print(e)


walk_result = walk(orig_path)
dirs = walk_result[1]
files = walk_result[2]
confirm_paths(orig_path, new_path)
# create_dirs(dirs, orig_path, new_path)