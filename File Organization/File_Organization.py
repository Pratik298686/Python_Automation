import os
import shutil
import sys

# Define a dictionary to map file extension to their repective folder
file_extension_mapping = {
    '.jpg' : 'Images',
    '.png' : 'Images',
    '.jpeg' : 'Images',
    '.gif' : 'Images',
    '.pdf' : 'Documents',
    '.doc' : 'Documents',
    'docx' : 'Documents',
    '.txt' : 'Documents',
    '.mp4' : 'Videos',
    '.avi' : 'Videos',
    '.mkv' : 'Videos',
    '.mov' : 'Videos'
}

def organize_files(source_folder, destination_folder):
    """
    Organizes files in a source folder into subfolders based on their types and moves them to a destination folder.
    
    Args:
        source_folder (str): The path to the source folder.
        destination_folder (str): The path to the destination folder.
    """
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if os.path.isfile(source_path):
            file_extension = os.path.splitext(filename)[1].lower()
            # print(file_extension)

            if file_extension in file_extension_mapping:
                destination_subfolder = file_extension_mapping[file_extension]
                destination_path = os.path.join(destination_folder, destination_subfolder)

                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)

                shutil.move(source_path, os.path.join(destination_path,filename))
                print(f"Moved {filename} to {destination_subfolder} folder")


def main():

    if len(sys.argv) != 3:
        print("Usage: python organize_files.py source_folder destination_folder")
        sys.exit(1)
    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]

    try:
        organize_files(source_folder, destination_folder)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
