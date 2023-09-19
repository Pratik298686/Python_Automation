# Automation script which accept directory name from user and remove duplicate files from that directory

from sys import *
import os
import hashlib
import time
import shutil

# Define a temporary directory to store deleted files
TEMP_DIR = r"C:\backup\Python\Deleted_files"
deleted_history = r"C:\backup\Python\Deleted_files\deleted_history.txt"

def DeleteFiless(dict1):
    results = list(filter(lambda x:len(x)>1, dict1.values()))

    icnt = 0

    if len(results)>0:
        deleted_files = []
        global TEMP_DIR
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    # os.remove(subresult)
                    try:
                        if not os.path.exists(TEMP_DIR):
                            os.makedirs(TEMP_DIR)
                        
                        new_path = os.path.join(TEMP_DIR, os.path.basename(subresult))
                        deleted_files.append(subresult)
                        shutil.move(subresult,new_path)  
                        print("Deleted File Path is: ",subresult)
                    except shutil.Error as e:
                        print(f"Shutil Error moving {subresult}: {str(e)}")
                    except FileNotFoundError as e:
                        print(f"File not found when moving {subresult}: {str(e)}")
                    except Exception as e:
                        print(f"Error moving {subresult}: {str(e)}") 

            icnt = 0
        log_deleted_files(deleted_files)
        
    else:
        print("No duplicate files found.")


def log_deleted_files(deleted_files):
    global deleted_history
    log_file = open(deleted_history, "a")
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    for file_path in deleted_files:
        log_file.write(f"{timestamp} - Deleted: {file_path}\n")
    log_file.close()

# Implement an undo function to move files back to their original location
def UndoDelete():
    global TEMP_DIR
    global deleted_history

    try:
        log_file = open(deleted_history, "r")
        lines = log_file.readlines()

        restored_files = []
        for line in lines:
            parts = line.strip().split(" - Deleted: ")
            if len(parts) == 2:
                timestamp, deleted_path = parts

                restored_path = os.path.join(TEMP_DIR, os.path.basename(deleted_path))
                if os.path.exists(restored_path):
                    shutil.move(restored_path,deleted_path) 
                    restored_files.append(deleted_path)
                    print(f"Restored: {deleted_path}")

        # Remove the entries from the history file for the files that were restored
        log_file = open(deleted_history, "w")
        for line in lines:
            parts = line.strip().split(" - Deleted: ")
            if len(parts) == 2:
                timestamp, deleted_path = parts
                if deleted_path not in restored_files:
                    log_file.write(line)
        print("Undo completed successfully.")
    except Exception as e:
        print(f"Error during undo: {str(e)}")


def hashfile(path, blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def findDup(path):
    flag = os.path.abspath(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    dups = {}

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid Path")

def printResults(dict1):
    results = list(filter(lambda x:len(x)>1, dict1.values()))

    if len(results) > 0:
        print("Duplicates Found: ")
        print("The following files are duplicate")
        for result in results:
            for subresult in result:
                print("\t\t%s"%subresult)
    else:
        print("No duplicate file found.")

def main():
    print("----- Marvellous Infosystems by Piyush Khairnar -----")

    print("Application name : "+argv[0])

    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1]=="-h" or argv[1]=="-H"):
        print("This Script is used to traverse specific directory and display sizes of files")
        exit()
    if(argv[1]=="-u" or argv[1]=="-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory Extention")
        exit()

    try:
        arr = {}
        startTime = time.time()
        arr = findDup(argv[1])
        printResults(arr)
        DeleteFiless(arr)
        endTime = time.time()

        print("Took %s seconds to evalute." % (endTime - startTime))
    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception as E:
        print("Error : Invalid input", E)

    # Ask the user if they want to undo the deletion
    user_choice = input("Do you want to undo the deletion? (yes/no): ")
    if user_choice.lower() == "yes":
        UndoDelete()
    else:
        print("Deletion not undone")

if __name__ == "__main__":
    main()